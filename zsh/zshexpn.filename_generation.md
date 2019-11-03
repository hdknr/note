# FILENAME GENERATION

       If  a  word contains an unquoted instance of one of the characters `*',
       `(', `|', `<', `[', or `?', it is regarded as a  pattern  for  filename
       generation,  unless  the  GLOB  option  is unset.  If the EXTENDED_GLOB
       option is set, the `^' and `#' characters also denote a pattern; other-
       wise they are not treated specially by the shell.

       The  word  is  replaced  with a list of sorted filenames that match the
       pattern.  If no matching pattern is found, the  shell  gives  an  error
       message,  unless the NULL_GLOB option is set, in which case the word is
       deleted; or unless the NOMATCH option is unset, in which case the  word
       is left unchanged.

       In  filename  generation, the character `/' must be matched explicitly;
       also, a `.' must be matched explicitly at the beginning of a pattern or
       after  a  `/', unless the GLOB_DOTS option is set.  No filename genera-
       tion pattern matches the files `.' or `..'.  In other instances of pat-
       tern matching, the `/' and `.' are not treated specially.

   Glob Operators
       *      Matches any string, including the null string.

       ?      Matches any character.

       [...]  Matches  any  of  the enclosed characters.  Ranges of characters
              can be specified by separating two characters by a `-'.   A  `-'
              or  `]' may be matched by including it as the first character in
              the list.  There are also several named classes  of  characters,
              in  the  form `[:name:]' with the following meanings.  The first
              set use the macros provided by the operating system to test  for
              the  given  character  combinations, including any modifications
              due to local language settings, see ctype(3):

              [:alnum:]
                     The character is alphanumeric

              [:alpha:]
                     The character is alphabetic

              [:ascii:]
                     The character is 7-bit, i.e. is a  single-byte  character
                     without the top bit set.

              [:blank:]
                     The character is a blank character

              [:cntrl:]
                     The character is a control character

              [:digit:]
                     The character is a decimal digit

              [:graph:]
                     The  character is a printable character other than white-
                     space

              [:lower:]
                     The character is a lowercase letter

              [:print:]
                     The character is printable

              [:punct:]
                     The character is printable but neither  alphanumeric  nor
                     whitespace

              [:space:]
                     The character is whitespace

              [:upper:]
                     The character is an uppercase letter

              [:xdigit:]
                     The character is a hexadecimal digit

              Another  set of named classes is handled internally by the shell
              and is not sensitive to the locale:

              [:IDENT:]
                     The character is allowed to form part of a shell  identi-
                     fier, such as a parameter name

              [:IFS:]
                     The  character  is used as an input field separator, i.e.
                     is contained in the IFS parameter

              [:IFSSPACE:]
                     The character is an IFS white space  character;  see  the
                     documentation for IFS in the zshparam(1) manual page.

              [:INCOMPLETE:]
                     Matches  a byte that starts an incomplete multibyte char-
                     acter.  Note that there may be a sequence  of  more  than
                     one bytes that taken together form the prefix of a multi-
                     byte character.  To test  for  a  potentially  incomplete
                     byte sequence, use the pattern `[[:INCOMPLETE:]]*'.  This
                     will never match a sequence starting with a valid  multi-
                     byte character.

              [:INVALID:]
                     Matches  a  byte  that  does  not start a valid multibyte
                     character.  Note this may be a continuation  byte  of  an
                     incomplete multibyte character as any part of a multibyte
                     string consisting of  invalid  and  incomplete  multibyte
                     characters is treated as single bytes.

              [:WORD:]
                     The  character is treated as part of a word; this test is
                     sensitive to the value of the WORDCHARS parameter

              Note that the square brackets are additional to those  enclosing
              the  whole  set  of characters, so to test for a single alphanu-
              meric character you need `[[:alnum:]]'.   Named  character  sets
              can be used alongside other types, e.g. `[[:alpha:]0-9]'.

       [^...]
       [!...] Like [...], except that it matches any character which is not in
              the given set.

       <[x]-[y]>
              Matches any number in the range x to y,  inclusive.   Either  of
              the  numbers  may be omitted to make the range open-ended; hence
              `<->' matches any number.  To match individual digits, the [...]
              form is more efficient.

              Be  careful  when  using other wildcards adjacent to patterns of
              this form; for example, <0-9>* will actually  match  any  number
              whatsoever  at  the  start of the string, since the `<0-9>' will
              match the first digit, and the `*' will match any others.   This
              is  a  trap  for the unwary, but is in fact an inevitable conse-
              quence of the rule that the longest possible match  always  suc-
              ceeds.   Expressions  such  as  `<0-9>[^[:digit:]]*' can be used
              instead.

       (...)  Matches the enclosed pattern.  This is used  for  grouping.   If
              the  KSH_GLOB  option  is  set, then a `@', `*', `+', `?' or `!'
              immediately preceding the `(' is treated specially, as  detailed
              below.  The  option SH_GLOB prevents bare parentheses from being
              used in this way, though the KSH_GLOB option is still available.

              Note  that  grouping cannot extend over multiple directories: it
              is an error to have a `/' within a group (this only applies  for
              patterns  used in filename generation).  There is one exception:
              a group of the form (pat/)# appearing as a complete path segment
              can match a sequence of directories.  For example, foo/(a*/)#bar
              matches foo/bar, foo/any/bar, foo/any/anyother/bar, and so on.

       x|y    Matches either x or y.  This operator has lower precedence  than
              any  other.   The  `|'  character must be within parentheses, to
              avoid interpretation as a pipeline.  The alternatives are  tried
              in order from left to right.

       ^x     (Requires EXTENDED_GLOB to be set.)  Matches anything except the
              pattern x.  This has a higher precedence than `/', so `^foo/bar'
              will  search  directories in `.' except `./foo' for a file named
              `bar'.

       x~y    (Requires EXTENDED_GLOB to be set.)  Match anything that matches
              the  pattern  x but does not match y.  This has lower precedence
              than any operator except `|', so `*/*~foo/bar' will  search  for
              all  files in all directories in `.'  and then exclude `foo/bar'
              if there was such a match.  Multiple patterns can be excluded by
              `foo~bar~baz'.   In  the  exclusion pattern (y), `/' and `.' are
              not treated specially the way they usually are in globbing.

       x#     (Requires EXTENDED_GLOB to be set.)  Matches zero or more occur-
              rences  of  the  pattern  x.  This operator has high precedence;
              `12#' is equivalent to `1(2#)', rather than `(12)#'.  It  is  an
              error  for  an  unquoted `#' to follow something which cannot be
              repeated; this includes an empty string, a pattern already  fol-
              lowed  by  `##',  or parentheses when part of a KSH_GLOB pattern
              (for example, `!(foo)#' is  invalid  and  must  be  replaced  by
              `*(!(foo))').

       x##    (Requires  EXTENDED_GLOB to be set.)  Matches one or more occur-
              rences of the pattern x.  This  operator  has  high  precedence;
              `12##' is equivalent to `1(2##)', rather than `(12)##'.  No more
              than two active `#' characters may appear together.   (Note  the
              potential  clash with glob qualifiers in the form `1(2##)' which
              should therefore be avoided.)

   ksh-like Glob Operators
       If the KSH_GLOB option is set, the effects of parentheses can be  modi-
       fied by a preceding `@', `*', `+', `?' or `!'.  This character need not
       be unquoted to have special effects, but the `(' must be.

       @(...) Match the pattern in the parentheses.  (Like `(...)'.)

       *(...) Match any number of occurrences.  (Like  `(...)#',  except  that
              recursive directory searching is not supported.)

       +(...) Match  at  least  one  occurrence.  (Like `(...)##', except that
              recursive directory searching is not supported.)

       ?(...) Match zero or one occurrence.  (Like `(|...)'.)

       !(...) Match  anything  but  the  expression  in  parentheses.    (Like
              `(^(...))'.)

   Precedence
       The precedence of the operators given above is (highest) `^', `/', `~',
       `|' (lowest); the remaining operators are simply treated from  left  to
       right  as  part of a string, with `#' and `##' applying to the shortest
       possible preceding unit (i.e. a character, `?', `[...]', `<...>', or  a
       parenthesised  expression).  As mentioned above, a `/' used as a direc-
       tory separator may not appear inside parentheses, while a `|'  must  do
       so;  in  patterns  used in other contexts than filename generation (for
       example, in case statements and tests within `[[...]]'), a `/'  is  not
       special;  and  `/'  is  also  not special after a `~' appearing outside
       parentheses in a filename pattern.

   Globbing Flags
       There are various flags which affect any text to their right up to  the
       end  of  the enclosing group or to the end of the pattern; they require
       the EXTENDED_GLOB option. All take the form (#X) where X may  have  one
       of the following forms:

       i      Case insensitive:  upper or lower case characters in the pattern
              match upper or lower case characters.

       l      Lower case characters in the pattern match upper or  lower  case
              characters;  upper  case  characters  in  the pattern still only
              match upper case characters.

       I      Case sensitive:  locally negates the effect of i or l from  that
              point on.

       b      Activate backreferences for parenthesised groups in the pattern;
              this does not work in filename generation.  When a pattern  with
              a  set  of active parentheses is matched, the strings matched by
              the groups are stored in the array $match, the  indices  of  the
              beginning  of  the matched parentheses in the array $mbegin, and
              the indices of the end in the array $mend, with the  first  ele-
              ment  of  each  array  corresponding  to the first parenthesised
              group, and so on.  These arrays are not otherwise special to the
              shell.   The  indices  use the same convention as does parameter
              substitution, so that elements of $mend and $mbegin may be  used
              in  subscripts;  the  KSH_ARRAYS  option  is respected.  Sets of
              globbing flags are not considered parenthesised groups; only the
              first nine active parentheses can be referenced.

              For example,

                     foo="a string with a message"
                     if [[ $foo = (a|an)' '(#b)(*)' '* ]]; then
                       print ${foo[$mbegin[1],$mend[1]]}
                     fi

              prints  `string  with  a'.   Note  that the first parenthesis is
              before the (#b) and does not create a backreference.

              Backreferences work with all forms  of  pattern  matching  other
              than  filename generation, but note that when performing matches
              on an entire array, such as ${array#pattern}, or a  global  sub-
              stitution,  such  as  ${param//pat/repl},  only the data for the
              last match remains available.  In the case  of  global  replace-
              ments  this may still be useful.  See the example for the m flag
              below.

              The numbering of backreferences strictly follows  the  order  of
              the  opening  parentheses  from  left  to  right  in the pattern
              string, although sets of parentheses may be nested.   There  are
              special rules for parentheses followed by `#' or `##'.  Only the
              last match of the parenthesis is remembered: for example, in `[[
              abab  =  (#b)([ab])#  ]]',  only  the  final  `b'  is  stored in
              match[1].  Thus extra parentheses may be necessary to match  the
              complete  segment:  for  example,  use `X((ab|cd)#)Y' to match a
              whole string of either `ab' or `cd' between `X' and  `Y',  using
              the value of $match[1] rather than $match[2].

              If the match fails none of the parameters is altered, so in some
              cases it may be necessary to  initialise  them  beforehand.   If
              some  of  the  backreferences  fail to match -- which happens if
              they are in an alternate branch which fails to match, or if they
              are  followed  by  #  and matched zero times -- then the matched
              string is set to the empty string, and the start and end indices
              are set to -1.

              Pattern  matching  with  backreferences  is slightly slower than
              without.

       B      Deactivate backreferences, negating the effect  of  the  b  flag
              from that point on.

       cN,M   The flag (#cN,M) can be used anywhere that the # or ## operators
              can be used except in the expressions `(*/)#'  and  `(*/)##'  in
              filename generation, where `/' has special meaning; it cannot be
              combined with other globbing  flags  and  a  bad  pattern  error
              occurs  if  it is misplaced.  It is equivalent to the form {N,M}
              in regular expressions.  The  previous  character  or  group  is
              required  to  match  between N and M times, inclusive.  The form
              (#cN) requires exactly N matches; (#c,M) is equivalent to speci-
              fying N as 0; (#cN,) specifies that there is no maximum limit on
              the number of matches.

       m      Set references to the match data for the entire string  matched;
              this is similar to backreferencing and does not work in filename
              generation.  The flag must be in effect at the end of  the  pat-
              tern, i.e. not local to a group. The parameters $MATCH,  $MBEGIN
              and $MEND will be set to the string matched and to  the  indices
              of  the  beginning and end of the string, respectively.  This is
              most useful in parameter substitutions, as otherwise the  string
              matched is obvious.

              For example,

                     arr=(veldt jynx grimps waqf zho buck)
                     print ${arr//(#m)[aeiou]/${(U)MATCH}}

              forces  all the matches (i.e. all vowels) into uppercase, print-
              ing `vEldt jynx grImps wAqf zhO bUck'.

              Unlike backreferences, there is no speed penalty for using match
              references,  other than the extra substitutions required for the
              replacement strings in cases such as the example shown.

       M      Deactivate the m flag, hence no references to match data will be
              created.

       anum   Approximate  matching:  num  errors  are  allowed  in the string
              matched by the pattern.  The rules for this are described in the
              next subsection.

       s, e   Unlike the other flags, these have only a local effect, and each
              must appear on its own:  `(#s)' and `(#e)' are  the  only  valid
              forms.   The  `(#s)' flag succeeds only at the start of the test
              string, and the `(#e)' flag succeeds only at the end of the test
              string;  they  correspond  to  `^'  and  `$' in standard regular
              expressions.  They are useful for matching path segments in pat-
              terns  other  than those in filename generation (where path seg-
              ments  are  in  any  case  treated  separately).   For  example,
              `*((#s)|/)test((#e)|/)*' matches a path segment `test' in any of
              the  following  strings:   test,   test/at/start,   at/end/test,
              in/test/middle.

              Another   use   is   in   parameter  substitution;  for  example
              `${array/(#s)A*Z(#e)}' will remove only  elements  of  an  array
              which match the complete pattern `A*Z'.  There are other ways of
              performing many operations of this type, however the combination
              of  the substitution operations `/' and `//' with the `(#s)' and
              `(#e)' flags provides a single simple and memorable method.

              Note that assertions of the form `(^(#s))' also work, i.e. match
              anywhere  except at the start of the string, although this actu-
              ally means `anything except a zero-length portion at  the  start
              of  the  string';  you  need  to  use  `(""~(#s))'  to  match  a
              zero-length portion of the string not at the start.

       q      A `q' and everything up to the closing parenthesis of the  glob-
              bing  flags  are  ignored by the pattern matching code.  This is
              intended to support the use of glob qualifiers, see below.   The
              result is that the pattern `(#b)(*).c(#q.)' can be used both for
              globbing and for matching against a string.  In the former case,
              the  `(#q.)'  will be treated as a glob qualifier and the `(#b)'
              will not be useful, while in the latter case the `(#b)' is  use-
              ful  for  backreferences  and the `(#q.)' will be ignored.  Note
              that colon modifiers in the glob qualifiers are also not applied
              in ordinary pattern matching.

       u      Respect the current locale in determining the presence of multi-
              byte characters in a pattern, provided the  shell  was  compiled
              with  MULTIBYTE_SUPPORT.   This  overrides the MULTIBYTE option;
              the default behaviour is taken  from  the  option.   Compare  U.
              (Mnemonic:  typically  multibyte  characters are from Unicode in
              the UTF-8 encoding, although any extension of ASCII supported by
              the system library may be used.)

       U      All  characters  are  considered  to be a single byte long.  The
              opposite of u.  This overrides the MULTIBYTE option.

       For example, the test string  fooxx  can  be  matched  by  the  pattern
       (#i)FOOXX,  but  not  by  (#l)FOOXX, (#i)FOO(#I)XX or ((#i)FOOX)X.  The
       string (#ia2)readme specifies case-insensitive matching of readme  with
       up to two errors.

       When  using the ksh syntax for grouping both KSH_GLOB and EXTENDED_GLOB
       must be set and the left parenthesis should be  preceded  by  @.   Note
       also that the flags do not affect letters inside [...] groups, in other
       words (#i)[a-z] still matches only lowercase  letters.   Finally,  note
       that when examining whole paths case-insensitively every directory must
       be searched for all files which match, so that a pattern  of  the  form
       (#i)/foo/bar/... is potentially slow.


   Approximate Matching
       When  matching  approximately,  the  shell  keeps a count of the errors
       found, which cannot exceed the number specified in the  (#anum)  flags.
       Four types of error are recognised:

       1.     Different characters, as in fooxbar and fooybar.

       2.     Transposition of characters, as in banana and abnana.

       3.     A  character  missing  in the target string, as with the pattern
              road and target string rod.

       4.     An extra character appearing in the target string, as with stove
              and strove.

       Thus,  the pattern (#a3)abcd matches dcba, with the errors occurring by
       using the first rule twice and the second once, grouping the string  as
       [d][cb][a] and [a][bc][d].

       Non-literal  parts of the pattern must match exactly, including charac-
       ters in character ranges: hence (#a1)???   matches  strings  of  length
       four,  by  applying  rule  4  to  an empty part of the pattern, but not
       strings of length two, since all the ? must  match.   Other  characters
       which  must  match  exactly  are  initial dots in filenames (unless the
       GLOB_DOTS option is set), and all slashes in filenames, so that a/bc is
       two errors from ab/c (the slash cannot be transposed with another char-
       acter).  Similarly, errors are counted  separately  for  non-contiguous
       strings in the pattern, so that (ab|cd)ef is two errors from aebf.

       When  using  exclusion  via  the  ~  operator,  approximate matching is
       treated entirely separately for the excluded part and must be activated
       separately.  Thus, (#a1)README~READ_ME matches READ.ME but not READ_ME,
       as the trailing READ_ME is  matched  without  approximation.   However,
       (#a1)README~(#a1)READ_ME does not match any pattern of the form READ?ME
       as all such forms are now excluded.

       Apart from exclusions, there is only one overall error count;  however,
       the  maximum  errors  allowed  may  be altered locally, and this can be
       delimited by grouping.  For example, (#a1)cat((#a0)dog)fox  allows  one
       error in total, which may not occur in the dog section, and the pattern
       (#a1)cat(#a0)dog(#a1)fox is equivalent.  Note that the point  at  which
       an  error is first found is the crucial one for establishing whether to
       use  approximation;  for  example,  (#a1)abc(#a0)xyz  will  not   match
       abcdxyz,  because  the  error occurs at the `x', where approximation is
       turned off.

       Entire  path  segments  may   be   matched   approximately,   so   that
       `(#a1)/foo/d/is/available/at/the/bar' allows one error in any path seg-
       ment.  This is much less efficient than  without  the  (#a1),  however,
       since  every  directory  in  the  path  must  be scanned for a possible
       approximate match.  It is best to place the (#a1) after any  path  seg-
       ments which are known to be correct.


   Recursive Globbing
       A pathname component of the form `(foo/)#' matches a path consisting of
       zero or more directories matching the pattern foo.

       As a shorthand, `**/' is equivalent to `(*/)#'; note that  this  there-
       fore  matches files in the current directory as well as subdirectories.
       Thus:

              ls (*/)#bar

       or

              ls **/bar

       does a recursive directory search for files  named  `bar'  (potentially
       including the file `bar' in the current directory).  This form does not
       follow symbolic links; the alternative form `***/' does, but is  other-
       wise  identical.   Neither of these can be combined with other forms of
       globbing within the same path segment; in that case, the `*'  operators
       revert to their usual effect.

       Even  shorter  forms  are  available when the option GLOB_STAR_SHORT is
       set.  In that case if no / immediately follows a **  or  ***  they  are
       treated as if both a / plus a further * are present.  Hence:

              setopt GLOBSTARSHORT
              ls **.c

       is equivalent to

              ls **/*.c

   Glob Qualifiers
       Patterns  used  for filename generation may end in a list of qualifiers
       enclosed in parentheses.  The qualifiers specify which  filenames  that
       otherwise  match  the  given  pattern  will be inserted in the argument
       list.

       If the option BARE_GLOB_QUAL is set, then a trailing set of parentheses
       containing  no `|' or `(' characters (or `~' if it is special) is taken
       as a set of glob qualifiers.  A glob subexpression that would  normally
       be  taken  as  glob qualifiers, for example `(^x)', can be forced to be
       treated as part of the glob pattern by  doubling  the  parentheses,  in
       this case producing `((^x))'.

       If  the option EXTENDED_GLOB is set, a different syntax for glob quali-
       fiers is available, namely `(#qx)' where x is  any  of  the  same  glob
       qualifiers  used in the other format.  The qualifiers must still appear
       at the end of the pattern.  However, with  this  syntax  multiple  glob
       qualifiers  may be chained together.  They are treated as a logical AND
       of the individual sets of flags.  Also, as the syntax  is  unambiguous,
       the  expression  will  be  treated  as glob qualifiers just as long any
       parentheses contained within it are balanced; appearance of `|', `(' or
       `~'  does  not  negate the effect.  Note that qualifiers will be recog-
       nised in this form even if a bare glob qualifier exists at the  end  of
       the  pattern, for example `*(#q*)(.)' will recognise executable regular
       files if both options are set; however, mixed syntax should probably be
       avoided for the sake of clarity.  Note that within conditions using the
       `[[' form the presence of a parenthesised expression (#q...) at the end
       of a string indicates that globbing should be performed; the expression
       may include glob qualifiers, but it is also valid if it is simply (#q).
       This  does  not apply to the right hand side of pattern match operators
       as the syntax already has special significance.

       A qualifier may be any one of the following:

       /      directories

       F      `full' (i.e. non-empty) directories.   Note  that  the  opposite
              sense (^F) expands to empty directories and all non-directories.
              Use (/^F) for empty directories.

       .      plain files

       @      symbolic links

       =      sockets

       p      named pipes (FIFOs)

       *      executable plain files (0100 or 0010 or 0001)

       %      device files (character or block special)

       %b     block special files

       %c     character special files

       r      owner-readable files (0400)

       w      owner-writable files (0200)

       x      owner-executable files (0100)

       A      group-readable files (0040)

       I      group-writable files (0020)

       E      group-executable files (0010)

       R      world-readable files (0004)

       W      world-writable files (0002)

       X      world-executable files (0001)

       s      setuid files (04000)

       S      setgid files (02000)

       t      files with the sticky bit (01000)

       fspec  files with access rights matching spec. This spec may be a octal
              number optionally preceded by a `=', a `+', or a `-'. If none of
              these characters is given, the behavior is the same as for  `='.
              The octal number describes the mode bits to be expected, if com-
              bined with a `=', the value  given  must  match  the  file-modes
              exactly,  with a `+', at least the bits in the given number must
              be set in the file-modes, and with a `-', the bits in the number
              must  not be set. Giving a `?' instead of a octal digit anywhere
              in the  number  ensures  that  the  corresponding  bits  in  the
              file-modes  are  not checked, this is only useful in combination
              with `='.

              If the qualifier `f' is followed by any other character anything
              up  to the next matching character (`[', `{', and `<' match `]',
              `}', and `>' respectively, any other character  matches  itself)
              is  taken  as a list of comma-separated sub-specs. Each sub-spec
              may be either an octal number as described above or  a  list  of
              any of the characters `u', `g', `o', and `a', followed by a `=',
              a `+', or a `-', followed by a list of  any  of  the  characters
              `r',  `w',  `x', `s', and `t', or an octal digit. The first list
              of characters specify which access rights are to be checked.  If
              a  `u'  is given, those for the owner of the file are used, if a
              `g' is given, those of the group are checked,  a  `o'  means  to
              test  those  of  other users, and the `a' says to test all three
              groups. The `=', `+', and `-' again says how the modes are to be
              checked  and  have  the  same meaning as described for the first
              form above. The second list of  characters  finally  says  which
              access  rights  are to be expected: `r' for read access, `w' for
              write access, `x' for the right  to  execute  the  file  (or  to
              search a directory), `s' for the setuid and setgid bits, and `t'
              for the sticky bit.

              Thus, `*(f70?)' gives the files for which the  owner  has  read,
              write, and execute permission, and for which other group members
              have no rights, independent of the permissions for other  users.
              The  pattern `*(f-100)' gives all files for which the owner does
              not have execute permission,  and  `*(f:gu+w,o-rx:)'  gives  the
              files  for  which  the  owner and the other members of the group
              have at least write permission, and for which other users  don't
              have read or execute permission.

       estring
       +cmd   The string will be executed as shell code.  The filename will be
              included in the list if and only if the code returns a zero sta-
              tus (usually the status of the last command).

              In  the  first  form,  the first character after the `e' will be
              used as a separator and anything up to the next matching separa-
              tor  will  be taken  as the string; `[', `{', and `<' match `]',
              `}', and `>', respectively, while any  other  character  matches
              itself.  Note  that  expansions  must be quoted in the string to
              prevent them  from  being  expanded  before  globbing  is  done.
              string  is  then executed as shell code.  The string globqual is
              appended to the array zsh_eval_context the  duration  of  execu-
              tion.

              During  the  execution  of  string  the filename currently being
              tested is available in the parameter REPLY; the parameter may be
              altered  to a string to be inserted into the list instead of the
              original filename.  In addition, the parameter reply may be  set
              to an array or a string, which overrides the value of REPLY.  If
              set to an array, the latter is inserted into  the  command  line
              word by word.

              For   example,  suppose  a  directory  contains  a  single  file
              `lonely'.  Then the  expression  `*(e:'reply=(${REPLY}{1,2})':)'
              will cause the words `lonely1' and `lonely2' to be inserted into
              the command line.  Note the quoting of string.

              The form +cmd has the same  effect,  but  no  delimiters  appear
              around  cmd.   Instead,  cmd is taken as the longest sequence of
              characters following the + that are alphanumeric or  underscore.
              Typically cmd will be the name of a shell function that contains
              the appropriate test.  For example,

                     nt() { [[ $REPLY -nt $NTREF ]] }
                     NTREF=reffile
                     ls -l *(+nt)

              lists all files in the directory that have  been  modified  more
              recently than reffile.

       ddev   files on the device dev

       l[-|+]ct
              files having a link count less than ct (-), greater than ct (+),
              or equal to ct

       U      files owned by the effective user ID

       G      files owned by the effective group ID

       uid    files owned by user ID id if that is a  number.   Otherwise,  id
              specifies a user name: the character after the `u' will be taken
              as a separator and the string between it and the  next  matching
              separator will be taken as a user name.  The starting separators
              `[', `{', and `<' match the final separators `]', `}', and  `>',
              respectively;  any other character matches itself.  The selected
              files are those owned by this user.  For  example,  `u:foo:'  or
              `u[foo]' selects files owned by user `foo'.

       gid    like uid but with group IDs or names

       a[Mwhms][-|+]n
              files  accessed  exactly  n days ago.  Files accessed within the
              last n days are selected using a  negative  value  for  n  (-n).
              Files accessed more than n days ago are selected by a positive n
              value (+n).  Optional unit specifiers `M', `w', `h', `m' or  `s'
              (e.g.  `ah5') cause the check to be performed with months (of 30
              days), weeks, hours, minutes or seconds instead of days, respec-
              tively.  An explicit `d' for days is also allowed.

              Any  fractional  part  of the difference between the access time
              and the current part in the appropriate units is ignored in  the
              comparison.   For  instance,  `echo  *(ah-5)'  would  echo files
              accessed within the last five hours, while `echo *(ah+5)'  would
              echo  files  accessed  at least six hours ago, as times strictly
              between five and six hours are treated as five hours.

       m[Mwhms][-|+]n
              like the file access qualifier, except that  it  uses  the  file
              modification time.

       c[Mwhms][-|+]n
              like  the  file  access  qualifier, except that it uses the file
              inode change time.

       L[+|-]n
              files less than n bytes (-), more than n bytes (+), or exactly n
              bytes in length.

              If this flag is directly followed by a size specifier `k' (`K'),
              `m' (`M'), or `p' (`P') (e.g. `Lk-50') the  check  is  performed
              with  kilobytes,  megabytes,  or  blocks (of 512 bytes) instead.
              (On some systems additional specifiers are available  for  giga-
              bytes,  `g' or `G', and terabytes, `t' or `T'.) If a size speci-
              fier is used a file is regarded as "exactly"  the  size  if  the
              file size rounded up to the next unit is equal to the test size.
              Hence `*(Lm1)' matches files from 1 byte up to 1 Megabyte inclu-
              sive.  Note also that the set of files "less than" the test size
              only includes files that would  not  match  the  equality  test;
              hence `*(Lm-1)' only matches files of zero size.

       ^      negates all qualifiers following it

       -      toggles  between  making  the  qualifiers work on symbolic links
              (the default) and the files they point to

       M      sets the MARK_DIRS option for the current pattern

       T      appends a trailing qualifier mark to the filenames, analogous to
              the LIST_TYPES option, for the current pattern (overrides M)

       N      sets the NULL_GLOB option for the current pattern

       D      sets the GLOB_DOTS option for the current pattern

       n      sets the NUMERIC_GLOB_SORT option for the current pattern

       Yn     enables short-circuit mode: the pattern will expand to at most n
              filenames.  If more than n  matches  exist,  only  the  first  n
              matches in directory traversal order will be considered.

              Implies oN when no oc qualifier is used.

       oc     specifies how the names of the files should be sorted. If c is n
              they are sorted by name; if it is L they are sorted depending on
              the size (length) of the files; if l they are sorted by the num-
              ber of links; if a, m, or c they are sorted by the time  of  the
              last  access,  modification, or inode change respectively; if d,
              files in subdirectories  appear  before  those  in  the  current
              directory  at  each level of the search -- this is best combined
              with other criteria, for example `odon' to  sort  on  names  for
              files  within the same directory; if N, no sorting is performed.
              Note that a, m, and c compare the age against the current  time,
              hence the first name in the list is the youngest file. Also note
              that the modifiers ^ and - are used, so `*(^-oL)' gives  a  list
              of  all files sorted by file size in descending order, following
              any symbolic links.  Unless oN is used,  multiple  order  speci-
              fiers may occur to resolve ties.

              The  default  sorting is n (by name) unless the Y glob qualifier
              is used, in which case it is N (unsorted).

              oe and o+ are special cases; they are  each  followed  by  shell
              code, delimited as for the e glob qualifier and the + glob qual-
              ifier respectively (see above).  The code is executed  for  each
              matched  file  with  the  parameter REPLY set to the name of the
              file on entry and globsort appended  to  zsh_eval_context.   The
              code  should  modify  the  parameter  REPLY in some fashion.  On
              return, the value of the parameter is used instead of  the  file
              name  as  the string on which to sort.  Unlike other sort opera-
              tors, oe and o+ may be repeated, but note that the maximum  num-
              ber  of  sort  operators of any kind that may appear in any glob
              expression is 12.

       Oc     like `o', but sorts in descending order; i.e.  `*(^oc)'  is  the
              same  as  `*(Oc)' and `*(^Oc)' is the same as `*(oc)'; `Od' puts
              files in the current directory before those in subdirectories at
              each level of the search.

       [beg[,end]]
              specifies  which  of the matched filenames should be included in
              the returned list. The syntax is the  same  as  for  array  sub-
              scripts.  beg  and  the optional end may be mathematical expres-
              sions. As in parameter subscripting they may be negative to make
              them  count  from  the  last match backward. E.g.: `*(-OL[1,3])'
              gives a list of the names of the three largest files.

       Pstring
              The string will be prepended to each glob match  as  a  separate
              word.  string is delimited in the same way as arguments to the e
              glob qualifier described above.  The qualifier can be  repeated;
              the words are prepended separately so that the resulting command
              line contains the words in the same order they were given in the
              list of glob qualifiers.

              A typical use for this is to prepend an option before all occur-
              rences of a file name; for example, the pattern `*(P:-f:)'  pro-
              duces the command line arguments `-f file1 -f file2 ...'

              If  the  modifier  ^  is  active,  then  string will be appended
              instead of prepended.  Prepending and appending is done indepen-
              dently  so  both  can  be  used on the same glob expression; for
              example by writing `*(P:foo:^P:bar:^P:baz:)' which produces  the
              command line arguments `foo baz file1 bar ...'

       More  than one of these lists can be combined, separated by commas. The
       whole list matches if at least one of the sublists  matches  (they  are
       `or'ed,  the qualifiers in the sublists are `and'ed).  Some qualifiers,
       however, affect all matches generated, independent of  the  sublist  in
       which  they  are  given.   These are the qualifiers `M', `T', `N', `D',
       `n', `o', `O' and the subscripts given in brackets (`[...]').

       If a `:' appears in a qualifier list, the remainder of  the  expression
       in  parenthesis  is  interpreted  as a modifier (see the section `Modi-
       fiers' in the section `History  Expansion').   Each  modifier  must  be
       introduced  by a separate `:'.  Note also that the result after modifi-
       cation does not have to be an existing file.  The name of any  existing
       file  can  be  followed  by  a modifier of the form `(:...)' even if no
       actual filename generation is performed, although note that  the  pres-
       ence of the parentheses causes the entire expression to be subjected to
       any global pattern matching options such as NULL_GLOB. Thus:

              ls *(-/)

       lists all directories and symbolic links that point to directories, and

              ls *(-@)

       lists all broken symbolic links, and

              ls *(%W)

       lists all world-writable device files in the current directory, and

              ls *(W,X)

       lists  all  files  in  the current directory that are world-writable or
       world-executable, and

              echo /tmp/foo*(u0^@:t)

       outputs the basename of all root-owned files beginning with the  string
       `foo' in /tmp, ignoring symlinks, and

              ls *.*~(lex|parse).[ch](^D^l1)

       lists  all  files  having a link count of one whose names contain a dot
       (but not those starting with  a  dot,  since  GLOB_DOTS  is  explicitly
       switched off) except for lex.c, lex.h, parse.c and parse.h.

              print b*.pro(#q:s/pro/shmo/)(#q.:s/builtin/shmiltin/)

       demonstrates  how  colon  modifiers and other qualifiers may be chained
       together.  The ordinary qualifier `.' is applied first, then the  colon
       modifiers  in order from left to right.  So if EXTENDED_GLOB is set and
       the base pattern matches the regular file builtin.pro, the  shell  will
       print `shmiltin.shmo'.