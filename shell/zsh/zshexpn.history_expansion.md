# HISTORY EXPANSION

       History expansion allows you to use words from previous  command  lines
       in  the  command line you are typing.  This simplifies spelling correc-
       tions and the repetition of complicated commands or arguments.

       Immediately before execution, each command  is  saved  in  the  history
       list,  the  size of which is controlled by the HISTSIZE parameter.  The
       one most recent command is always retained in  any  case.   Each  saved
       command in the history list is called a history event and is assigned a
       number, beginning with 1 (one) when the shell starts up.   The  history
       number  that  you  may  see  in  your  prompt  (see EXPANSION OF PROMPT
       SEQUENCES in zshmisc(1)) is the number that is to be  assigned  to  the
       next command.

##   Overview

       A  history  expansion  begins with the first character of the histchars
       parameter, which is `!' by default, and may occur anywhere on the  com-
       mand line, including inside double quotes (but not inside single quotes
       '...' or C-style quotes $'...' nor when escaped with a backslash).

       The first character is followed by an optional  event  designator  (see
       the  section  `Event Designators') and then an optional word designator
       (the section `Word Designators'); if neither of  these  designators  is
       present, no history expansion occurs.

       Input  lines  containing  history  expansions  are  echoed  after being
       expanded, but before any other expansions take  place  and  before  the
       command  is executed.  It is this expanded form that is recorded as the
       history event for later references.

       History expansions do not nest.

       By default, a history reference with no event designator refers to  the
       same  event as any preceding history reference on that command line; if
       it is the only history reference in a command, it refers to the  previ-
       ous  command.   However,  if the option CSH_JUNKIE_HISTORY is set, then
       every history reference with no event specification  always  refers  to
       the previous command.

       For  example,  `!' is the event designator for the previous command, so
       `!!:1' always refers to the first word of  the  previous  command,  and
       `!!$'  always  refers  to  the last word of the previous command.  With
       CSH_JUNKIE_HISTORY set, then `!:1' and `!$' function in the same manner
       as  `!!:1'  and `!!$', respectively.  Conversely, if CSH_JUNKIE_HISTORY
       is unset, then `!:1' and `!$'  refer  to  the  first  and  last  words,
       respectively, of the same event referenced by the nearest other history
       reference preceding them on the current command line, or to the  previ-
       ous command if there is no preceding reference.

       The  character  sequence  `^foo^bar'  (where `^' is actually the second
       character of the histchars parameter) repeats the last command, replac-
       ing  the string foo with bar.  More precisely, the sequence `^foo^bar^'
       is synonymous with `!!:s^foo^bar^', hence other modifiers (see the sec-
       tion   `Modifiers')   may   follow   the  final  `^'.   In  particular,
       `^foo^bar^:G' performs a global substitution.

       If the shell encounters the character sequence `!"' in the  input,  the
       history  mechanism  is temporarily disabled until the current list (see
       zshmisc(1)) is fully parsed.  The `!"' is removed from the  input,  and
       any subsequent `!' characters have no special significance.

       A  less convenient but more comprehensible form of command history sup-
       port is provided by the fc builtin.


## Event Designators

       An event designator is a reference to a command-line entry in the  his-
       tory  list.   In  the list below, remember that the initial `!' in each
       item may be changed to  another  character  by  setting  the  histchars
       parameter.

       !      Start a history expansion, except when followed by a blank, new-
              line, `=' or `('.  If followed immediately by a word  designator
              (see  the section `Word Designators'), this forms a history ref-
              erence with no event designator (see the section `Overview').

       !!     Refer to  the  previous  command.   By  itself,  this  expansion
              repeats the previous command.

       !n     Refer to command-line n.

       !-n    Refer to the current command-line minus n.

       !str   Refer to the most recent command starting with str.

       !?str[?]
              Refer  to  the most recent command containing str.  The trailing
              `?' is necessary if this reference is to be followed by a  modi-
              fier  or  followed by any text that is not to be considered part
              of str.

       !#     Refer to the current command line typed in so far.  The line  is
              treated  as  if  it  were  complete up to and including the word
              before the one with the `!#' reference.

       !{...} Insulate a history reference from adjacent characters (if neces-
              sary).

## Word Designators

       A word designator indicates which word or words of a given command line
       are to be included in a history reference.  A `:' usually separates the
       event  specification  from the word designator.  It may be omitted only
       if the word designator begins with a `^', `$', `*', `-' or  `%'.   Word
       designators include:

       0      The first input word (command).
       n      The nth argument.
       ^      The first argument.  That is, 1.
       $      The last argument.
       %      The word matched by (the most recent) ?str search.
       x-y    A range of words; x defaults to 0.
       *      All the arguments, or a null value if there are none.
       x*     Abbreviates `x-$'.
       x-     Like `x*' but omitting word $.

       Note  that  a  `%' word designator works only when used in one of `!%',
       `!:%' or `!?str?:%', and only when used after a !? expansion  (possibly
       in  an  earlier  command).  Anything else results in an error, although
       the error may not be the most obvious one.

## Modifiers

       After the optional word designator, you can add a sequence  of  one  or
       more  of  the following modifiers, each preceded by a `:'.  These modi-
       fiers also work on the result  of  filename  generation  and  parameter
       expansion, except where noted.

       a      Turn  a  file  name into an absolute path:  prepends the current
              directory, if necessary; remove `.' path  segments;  and  remove
              `..'  path  segments  and  the segments that immediately precede
              them.

              This transformation is agnostic about what is in the filesystem,
              i.e.  is  on  the logical, not the physical directory.  It takes
              place in the same manner as when changing directories when  nei-
              ther of the options CHASE_DOTS or CHASE_LINKS is set.  For exam-
              ple,   `/before/here/../after'   is   always   transformed    to
              `/before/after',  regardless of whether `/before/here' exists or
              what kind of object (dir, file, symlink, etc.) it is.

       A      Turn a file name into an absolute path as the `a' modifier does,
              and  then  pass the result through the realpath(3) library func-
              tion to resolve symbolic links.

              Note: on systems that do not have a  realpath(3)  library  func-
              tion,  symbolic  links are not resolved, so on those systems `a'
              and `A' are equivalent.

              Note: foo:A and realpath(foo) are different on some inputs.  For
              realpath(foo) semantics, see the `P` modifier.

       c      Resolve  a  command  name into an absolute path by searching the
              command path given by the PATH variable.  This does not work for
              commands  containing  directory parts.  Note also that this does
              not usually work as a glob qualifier unless a file of  the  same
              name is found in the current directory.

       e      Remove  all but the part of the filename extension following the
              `.'; see  the  definition  of  the  filename  extension  in  the
              description  of  the  r  modifier below.  Note that according to
              that definition the result will be empty if the string ends with
              a `.'.

       h      Remove  a  trailing  pathname component, leaving the head.  This
              works like `dirname'.

       l      Convert the words to all lowercase.

       p      Print the new command but do not execute it.   Only  works  with
              history expansion.

       P      Turn  a  file name into an absolute path, like realpath(3).  The
              resulting path will be absolute, have neither `.' nor `..'  com-
              ponents,  and  refer  to  the  same directory entry as the input
              filename.

              Unlike realpath(3), non-existent trailing components are permit-
              ted and preserved.

       q      Quote  the  substituted  words,  escaping further substitutions.
              Works with history expansion and parameter expansion, though for
              parameters  it  is  only  useful  if the resulting text is to be
              re-evaluated such as by eval.

       Q      Remove one level of quotes from the substituted words.

       r      Remove a filename extension leaving the root name.  Strings with
              no  filename extension are not altered.  A filename extension is
              a `.' followed by any number of characters (including zero) that
              are  neither  `.'  nor  `/'  and that continue to the end of the
              string.  For example, the extension of `foo.orig.c' is `.c', and
              `dir.c/foo' has no extension.

       s/l/r[/]
              Substitute r for l as described below.  The substitution is done
              only for the first string that matches l.  For  arrays  and  for
              filename  generation,  this applies to each word of the expanded
              text.  See below for further notes on substitutions.

              The forms `gs/l/r' and `s/l/r/:G' perform  global  substitution,
              i.e. substitute every occurrence of r for l.  Note that the g or
              :G must appear in exactly the position shown.

              See further notes on this form of substitution below.

       &      Repeat the previous s substitution.  Like  s,  may  be  preceded
              immediately  by  a  g.  In parameter expansion the & must appear
              inside braces, and in filename generation it must be quoted with
              a backslash.

       t      Remove  all leading pathname components, leaving the tail.  This
              works like `basename'.

       u      Convert the words to all uppercase.

       x      Like q, but break into words at whitespace.  Does not work  with
              parameter expansion.

       The  s/l/r/  substitution  works  as follows.  By default the left-hand
       side of substitutions are not patterns,  but  character  strings.   Any
       character  can  be  used as the delimiter in place of `/'.  A backslash
       quotes  the  delimiter  character.    The   character   `&',   in   the
       right-hand-side  r,  is replaced by the text from the left-hand-side l.
       The `&' can be quoted with a backslash.  A null  l  uses  the  previous
       string  either from the previous l or from the contextual scan string s
       from `!?s'.  You can omit the rightmost delimiter if a newline  immedi-
       ately  follows  r; the rightmost `?' in a context scan can similarly be
       omitted.  Note the same record of the last l and r is maintained across
       all forms of expansion.

       Note that if a `&' is used within glob qualifiers an extra backslash is
       needed as a & is a special character in this case.

       Also note that the order of expansions affects the interpretation of  l
       and r.  When used in a history expansion, which occurs before any other
       expansions, l and r are treated as literal strings (except as explained
       for  HIST_SUBST_PATTERN  below).  When used in parameter expansion, the
       replacement of r into the parameter's value is done first, and then any
       additional process, parameter, command, arithmetic, or brace references
       are applied, which may evaluate those substitutions and expansions more
       than once if l appears more than once in the starting value.  When used
       in a glob qualifier, any substitutions or expansions are performed once
       at  the  time  the qualifier is parsed, even before the `:s' expression
       itself is divided into l and r sides.

       If the option HIST_SUBST_PATTERN is set, l is treated as a  pattern  of
       the  usual  form  described  in  the section FILENAME GENERATION below.
       This can be used in all the places where modifiers are available; note,
       however, that in globbing qualifiers parameter substitution has already
       taken place, so parameters in the replacement string should  be  quoted
       to  ensure  they are replaced at the correct time.  Note also that com-
       plicated patterns used in globbing qualifiers  may  need  the  extended
       glob  qualifier notation (#q:s/.../.../) in order for the shell to rec-
       ognize the expression as a glob qualifier.  Further, note that bad pat-
       terns  in the substitution are not subject to the NO_BAD_PATTERN option
       so will cause an error.

       When HIST_SUBST_PATTERN is set, l may start with a # to  indicate  that
       the  pattern  must  match at the start of the string to be substituted,
       and a % may appear at the start or after an # to indicate that the pat-
       tern must match at the end of the string to be substituted.  The % or #
       may be quoted with two backslashes.

       For example, the following piece of filename generation code  with  the
       EXTENDED_GLOB option:

              print *.c(#q:s/#%(#b)s(*).c/'S${match[1]}.C'/)

       takes  the  expansion  of  *.c  and  applies the glob qualifiers in the
       (#q...) expression, which consists of a substitution modifier  anchored
       to  the  start and end of each word (#%).  This turns on backreferences
       ((#b)), so that the parenthesised subexpression  is  available  in  the
       replacement string as ${match[1]}.  The replacement string is quoted so
       that the parameter is not substituted before the start of filename gen-
       eration.

       The  following  f, F, w and W modifiers work only with parameter expan-
       sion and filename generation.  They are listed here to provide a single
       point of reference for all modifiers.

       f      Repeats  the  immediately  (without  a colon) following modifier
              until the resulting word doesn't change any more.

       F:expr:
              Like f, but repeats only n times if the expression  expr  evalu-
              ates  to  n.   Any  character can be used instead of the `:'; if
              `(', `[', or `{' is used as the opening delimiter,  the  closing
              delimiter should be ')', `]', or `}', respectively.

       w      Makes  the  immediately  following modifier work on each word in
              the string.

       W:sep: Like w but words are considered to be the parts  of  the  string
              that  are separated by sep. Any character can be used instead of
              the `:'; opening parentheses are handled specially, see above.