#!/usr/bin/python
# $Id: $

# Converts Oracle, SQL-Server, and other DDL to Snowflake DDL


def usage():
    print """\
# Usage: sql2sf.py input-file [output-file]
    """

import sys
import traceback
import etl_util
import os, glob, errno
import shutil
import cStringIO, string, re
from string import maketrans
import argparse

### RegExes for Oracle dialect that Snowflake doesn't support

# VARCHAR2(n BYTE) => VARCHAR(n)
varchar2_re = re.compile('(.*)(VARCHAR2\((\d+)(\s+.+)?\))(.*)', re.IGNORECASE)

# CHAR(n BYTE) => CHAR(n)
char_re = re.compile('(.*)(CHAR\((\d+)(\s+.+)\))(.*)', re.IGNORECASE)

# DEFAULT SYSDATE => deleted (OK only because data loaded from table should already have date)
# Snowflake DEFAULT must be literal
default_sysdate_re = re.compile('(.*)\ (DEFAULT SYSDATE)\ (.*)', re.IGNORECASE)

# SYSDATE => CURRENT_TIMESTAMP()
#sysdate_re = re.compile('(.*)\ (SYSDATE)\ (.*)', re.IGNORECASE)
sysdate_re = re.compile('(.*[,\(\s])(SYSDATE)([,\)\s].*)', re.IGNORECASE)

# SEGMENT CREATION type => ignore
segment_creation_re = re.compile('(.*)\ (SEGMENT\s+CREATION\s+(?:IMMEDIATE|DEFERRED))(.*)', re.IGNORECASE)

# NOT NULL ENABLE => NOT NULL
not_null_enable_re = re.compile('(.*)(NOT\s+NULL\s+ENABLE)(.*)', re.IGNORECASE)

# find prior period, e.g. trunc(col,'MM')-1 => dateadd('MM', -1, trunc(col, 'MM'))
prior_period_re = re.compile('(.*)(TRUNC\(\s*(.+?),\s*(\'.+?\')\s*\)\s*(-?\s*\d+))(.*)', re.IGNORECASE)

# add months, e.g. add_months(trunc(col, 'MM'), -5) => dateadd(month, -5, col)
add_months_re = re.compile('(.*)(ADD_MONTHS\(\s*TRUNC\(\s*(.+?),\s*(\'.+?\')\s*\),\s*(-?\s*\d+))(.*)', re.IGNORECASE)


### RegExes for SQL-Server dialect that Snowflake doesn't support

# NULL (explicit NULL constraint) -- ignore
null_constraint_re = re.compile('(.*)((?<!NOT)\s+NULL(?!::))(.*)', re.IGNORECASE)
is_null_condition_re = re.compile('.*IS NULL.*', re.IGNORECASE)

# NVARCHAR => VARCHAR
nvarchar_re = re.compile('(.*)\ (NVARCHAR)(.*)', re.IGNORECASE)

# NVARCHAR => VARCHAR
nchar_re = re.compile('(.*)\ (NCHAR)(.*)', re.IGNORECASE)

# ON PRIMARY => ignore
on_primary_re = re.compile('(.*)\ (ON PRIMARY)(.*)', re.IGNORECASE)

# DATETIME => TIMESTAMP
datetime_re = re.compile('(.*)\ (DATETIME)(.*)', re.IGNORECASE)

# BIT => BOOLEAN
bit_re = re.compile('(.*)\ (BIT)(.*)', re.IGNORECASE)


### RegExes for Redshift dialect that Snowflake doesn't support

# DISTKEY(col) => ignore
# DISTKEY => ignore
distkey_re = re.compile('(.*)(\s*DISTKEY\s*(?:\(.*?\))?)(.*)', re.IGNORECASE)

# SORTKEY(col) => ignore
sortkey_re = re.compile('(.*)(\s*SORTKEY\s*\(.*?\))(.*)', re.IGNORECASE)

# SORTKEY => ignore through end of statement
sortkey_multiline_re = re.compile('(.*)(\s*SORTKEY\s*\(?\s*$)(.*)', re.IGNORECASE)

# ENCODE type => ignore
encode_re = re.compile('(.*)(\sENCODE\s+.+?)((?:,|\s+|$).*)', re.IGNORECASE)

# DISTSTYLE type => ignore
diststyle_re = re.compile('(.*)(\s*DISTSTYLE\s+.+?)((?:,|\s+|$).*)', re.IGNORECASE)

# 'now'::character varying => current_timestamp
now_character_varying_re = re.compile('(.*)(\'now\'::(?:character varying|text))(.*)', re.IGNORECASE)

# bpchar => char
bpchar_re = re.compile('(.*)(bpchar)(.*)', re.IGNORECASE)

# character varying => varchar
character_varying_re = re.compile('(.*)(character varying)(.*)')

# interleaved => ignore
interleaved_re = re.compile('(.*)(interleaved)(.*)', re.IGNORECASE)

# identity(start, 0, ([0-9],[0-9])::text) => identity(start, 1)
identity_re = re.compile('(.*)\s*DEFAULT\s*"identity"\(([0-9]*),.*?(?:.*?::text)\)(.*)', re.IGNORECASE)

### RegExes for Netezza dialect that Snowflake doesn't support

## casting syntax
# INT4(expr) => expr::INTEGER
int4_re = re.compile('(.*)\ (INT4\s*\((.*?)\))(.*)', re.IGNORECASE)

### RegExes for common/standard types that Snowflake doesn't support
bigint_re = re.compile('(.*)\ (BIGINT)(.*)', re.IGNORECASE)
smallint_re = re.compile('(.*)\ (SMALLINT)(.*)', re.IGNORECASE)
floatN_re = re.compile('(.*)\ (FLOAT\d+)(.*)', re.IGNORECASE)

# CREATE [type] INDEX => ignore through end of statement
index_re = re.compile('(.*)(CREATE(?:\s+(?:UNIQUE|BITMAP))?\ INDEX)(.*)', re.IGNORECASE)

# ALTER TABLE ... ADD PRIMARY KEY => ignore
pk_re = re.compile('(.*)(ALTER\s+TABLE\s+.*ADD\s+PRIMARY\s+KEY)(.*)', re.IGNORECASE)

# SET ... TO => ignore
set_re = re.compile('(.*)(SET\s+.*TO)(.*)', re.IGNORECASE)


statement_term_re = re.compile('(.*);(.*)', re.IGNORECASE)

def make_snow(sqlin, sqlout, no_comments):
    ### processing mode
    comment_lines = None
    term_re = None

    for line in sqlin:
        ### state variables
        pre = None
        clause = None
        post = None
        comment = None

        sql = line.rstrip()
        sql = sql.replace('[', '').replace(']', '')

        # print >> sys.stdout, 'input: ' + sql

        if comment_lines:
            result = term_re.match(sql)
            if result:
                comment_lines = None
                term_re = None
            sql = '-- {0}'.format(sql)

        # VARCHAR2(n BYTE) => VARCHAR(n)
        result = varchar2_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)     # varchar2 clause
            cnt = result.group(3)
            discard = result.group(4)
            post = result.group(5)
            sql = '{0}{1}({2}){3}\t\t-- {4}'.format(pre, clause[0:7], cnt, post, clause)

        # CHAR(n BYTE) => CHAR(n)
        result = char_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)     # char clause
            cnt = result.group(3)
            discard = result.group(4)
            post = result.group(5)
            sql = '{0}{1}({2}){3}\t\t-- {4}'.format(pre, clause[0:4], cnt, post, clause)

        # DEFAULT SYSDATE => deleted (OK only because data loaded from table should already have date)
        result = default_sysdate_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0} {1}\t\t-- {2}'.format(pre, post, clause)

        # NVARCHAR => VARCHAR
        result = nvarchar_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0} VARCHAR {1}\t\t-- {2}'.format(pre, post, clause)

        # NCHAR => CHAR
        result = nchar_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0} CHAR {1}\t\t-- {2}'.format(pre, post, clause)

        # DATETIME => TIMESTAMP
        result = datetime_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0} TIMESTAMP {1}\t\t-- {2}'.format(pre, post, clause)

        # BIGINT => INTEGER
        #result = bigint_re.match(sql)
        #if result:
        #    pre = result.group(1)
        #    clause = result.group(2)
        #    post = result.group(3)
        #    sql = '{0} INTEGER {1}\t\t-- {2}'.format(pre, post, clause)

        # SMALLINT => INTEGER
        #result = smallint_re.match(sql)
        #if result:
        #    pre = result.group(1)
        #    clause = result.group(2)
        #    post = result.group(3)
        #    sql = '{0} INTEGER {1}\t\t-- {2}'.format(pre, post, clause)

        # BIT => BOOLEAN
        result = bit_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0} BOOLEAN {1}\t\t-- {2}'.format(pre, post, clause)

        # FLOAT8 => FLOAT
        result = floatN_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0} FLOAT {1}\t\t-- {2}'.format(pre, post, clause)

        # NULL (without NOT) => implicit nullable
        result = null_constraint_re.match(sql)
        if result and is_null_condition_re.match(sql):
            # we are in query or DML, so not looking at a constraint
            result = None
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}{1}\t\t-- {2}'.format(pre, post, clause)

        # ON PRIMARY => ignore
        result = on_primary_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}{1}\t\t-- {2}'.format(pre, post, clause)

        # DISTKEY(col) => ignore
        result = distkey_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}{1}\t\t-- {2}'.format(pre, post, clause)

        # SORTKEY(col) => ignore
        result = sortkey_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}{1}\t\t-- {2}'.format(pre, post, clause)

        # SORTKEY => ignore through end of statement
        result = sortkey_multiline_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0};\n-- {2} {1}'.format(pre, post, clause)
            comment_lines = 1
            term_re = statement_term_re

        # ENCODE type => ignore
        result = encode_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}{1}\t\t-- {2}'.format(pre, post, clause)

        # DISTSTYLE type => ignore
        result = diststyle_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}{1}\t\t-- {2}'.format(pre, post, clause)

        # 'now'::(character varying|text) => current_timestamp
        result = now_character_varying_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}CURRENT_TIMESTAMP{1} --{2}'.format(pre,post,clause)

        # bpchar => char
        result = bpchar_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}char{1} --{2}'.format(pre,post,clause)

        result = character_varying_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}varchar{1}  --{2}'.format(pre,post,clause)

        # interleaved => ignore
        result = interleaved_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0} {1} --{2}'.format(pre,post,clause)

        result = identity_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0} IDENTITY({1},1) {2}'.format(pre,clause,post)

        # SEGMENT CREATION type => ignore
        result = segment_creation_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0};;\n-- {2} {1}'.format(pre, post, clause)
            comment_lines = 1
            term_re = statement_term_re

        # ALTER TABLE ... ADD PRIMARY KEY => ignore
        result = index_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}-- {2} {1}'.format(pre, post, clause)
            comment_lines = 1
            term_re = statement_term_re

        # INDEX CREATION => ignore through end of statement
        result = pk_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}-- {2} {1}'.format(pre, post, clause)
            comment_lines = 1
            term_re = statement_term_re

        # SET ... TO => ignore
        result = set_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}-- {2} {1}'.format(pre, post, clause)
            comment_lines = 1
            term_re = statement_term_re

        # NOT NULL ENABLE => NOT NULL
        result = not_null_enable_re.match(sql)
        if result:
            pre = result.group(1)
            clause = result.group(2)
            post = result.group(3)
            sql = '{0}NOT NULL{1}\t\t-- {2}'.format(pre, post, clause)

        ## DML transformations that might appear multiple times per line
        dml_repeat = True
        while dml_repeat:
            dml_repeat = False

            # determine prior period
            # e.g. trunc(sysdate,'MM')-1
            result = prior_period_re.match(sql)
            if result:
                pre = result.group(1)
                clause = result.group(2)
                col = result.group(3)
                units = result.group(4)
                offset = result.group(5)
                post = result.group(6)
                sql = '{0}dateadd({4}, {5}, trunc({3}, {4}))'.format(pre, post, clause, col, units, offset)
                comment = append_comment(comment, clause, no_comments)
                dml_repeat = True

            # add_months
            # e.g. add_months(trunc(sysdate, 'MM'), -5) => dateadd('MM', -5, trunc(current_timestamp, 'MM'))
            result = add_months_re.match(sql)
            if result:
                raise Exception("Snowflake now has add_months() function -- verify can use as-is")

            # SYSDATE => CURRENT_TIMESTAMP()
            result = sysdate_re.match(sql)
            if result:
                pre = result.group(1)
                clause = result.group(2)
                post = result.group(3)
                sql = '{0} CURRENT_TIMESTAMP() {1}'.format(pre, post, clause)
                comment = append_comment(comment, clause, no_comments)
                dml_repeat = True

            # INT4(expr) => expr::INTEGER
            result = int4_re.match(sql)
            if result:
                pre = result.group(1)
                clause = result.group(2)
                col = result.group(3)
                post = result.group(4)
                sql = '{0} {3}::integer {1}'.format(pre, post, clause, col)
                comment = append_comment(comment, clause, no_comments)
                dml_repeat = True

        # write out possibly modified line
        sqlout.write(sql)
        if comment:
            sqlout.write('\t\t-- {0}'.format(comment))
        sqlout.write('\n')
        continue

def append_comment(old_comment, new_comment, no_comments):
    if no_comments:
        return None
    if old_comment and new_comment:
        return '{0} // {1}'.format(old_comment, new_comment)
    if not old_comment:
        return new_comment
    return old_comment

##### MAIN #####
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Convert SQL dialects to Snowflake.')
    parser.add_argument('--no_comments', action='store_true',
        help='suppress comments with changes (default: show changes)')
    parser.add_argument('inputfile', action='store', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
        help='input SQL file in other-vendor dialect (default: stdin)')
    parser.add_argument('outputfile', action='store', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
        help='output SQL file in Snowflake dialect (default: stdout)')
    args=parser.parse_args();
    print >> sys.stderr, "no_comments = " + str(args.no_comments)
    print >> sys.stderr, "input: " + str(args.inputfile.name)
    print >> sys.stderr, "output: " + str(args.outputfile.name)

    with etl_util.error_reporting():
        make_snow(args.inputfile, args.outputfile, args.no_comments)
        args.inputfile.close()
        args.outputfile.close()
        print >> sys.stderr, "done translating " + args.inputfile.name
