# Parameter Expansion Flags

If the opening brace is directly followed by an opening parenthesis,
the string up to the matching closing parenthesis will be taken as a list of flags.

~~~zsh
{(flag) .....}
~~~

In cases where repeating a flag is meaningful,
the repetitions need not be consecutive;
for example, `(q%q%q)` means the same thing as the more readable `(%%qqq)`.

The following flags are supported:

## `#` (数値の文字化)

Evaluate the resulting words as numeric expressions and output the characters corresponding to the resulting integer.
Note that this form is entirely distinct from use of the # without parentheses.

~~~zsh
a0=65
a1=97

echo ${(#)a0} , ${(#)a1}
~~~

~~~zsh
A , a
~~~

If the `MULTIBYTE` option is set and the number is greater than 127 (i.e. not an ASCII character)
it is treated as a Unicode character.

## `%`

Expand all `%` escapes in the resulting words in the same way as in prompts (see EXPANSION OF PROMPT SEQUENCES in zshmisc(1)).

If this flag is given twice,
full prompt expansion is done  on  the resulting words, depending on the setting of the PROMPT_PERCENT,
PROMPT_SUBST and PROMPT_BANG options.

## `@`

In double quotes, array elements are put into separate words.

E.g., `"${(@)foo}"` is equivalent to `"${foo[@]}"` and `"${(@)foo[1,2]}"` is the same as `"$foo[1]" "$foo[2]"`.
This is distinct from field splitting by the f, s or z flags, which still applies within each array element.

## `A`

      Convert the substitution into an array expression,  even  if  it
              otherwise  would be scalar.  This has lower precedence than sub-
              scripting, so one level of nested expansion is required in order
              that  subscripts apply to array elements.  Thus ${${(A)name}[1]}
              yields the full value of name when name is scalar.

              This assigns an array parameter with `${...=...}', `${...:=...}'
              or  `${...::=...}'.   If  this  flag  is  repeated (as in `AA'),
              assigns an associative  array  parameter.   Assignment  is  made
              before  sorting  or  padding;  if field splitting is active, the
              word part is split before assignment.  The name part  may  be  a
              subscripted  range  for ordinary arrays; when assigning an asso-
              ciative array, the word part must be converted to an array,  for
              example by using `${(AA)=name=...}' to activate field splitting.

              Surrounding context such as additional nesting  or  use  of  the
              value  in  a  scalar assignment may cause the array to be joined
              back into a single string again.

## `a`

       a      Sort in array index  order;  when  combined  with  `O'  sort  in
              reverse  array  index order.  Note that `a' is therefore equiva-
              lent to the default but `Oa' is useful for obtaining an  array's
              elements in reverse order.

## `b`

       b      Quote  with backslashes only characters that are special to pat-
              tern matching. This is useful when the contents of the  variable
              are to be tested using GLOB_SUBST, including the ${~...} switch.

              Quoting using one of the q family of flags  does  not  work  for
              this  purpose  since  quotes  are  not stripped from non-pattern
              characters by GLOB_SUBST.  In other words,

                     pattern=${(q)str}
                     [[ $str = ${~pattern} ]]

              works if $str is `a*b' but not if it is `a b', whereas

                     pattern=${(b)str}
                     [[ $str = ${~pattern} ]]

              is always true for any possible value of $str.

## `c`

       c      With ${#name}, count the total number of characters in an array,
              as  if  the elements were concatenated with spaces between them.
              This is not a true join of the array, so other expressions  used
              with  this  flag may have an effect on the elements of the array
              before it is counted.

## `C`

       C      Capitalize the resulting words.  `Words' in this case refers  to
              sequences  of  alphanumeric characters separated by non-alphanu-
              merics, not to words that result from field splitting.

## `D`

       D      Assume the string or  array  elements  contain  directories  and
              attempt  to  substitute the leading part of these by names.  The
              remainder of the path (the whole of it if the leading  part  was
              not  substituted) is then quoted so that the whole string can be
              used as a shell argument.  This is the reverse of `~'  substitu-
              tion:  see the section FILENAME EXPANSION below.

## `e`

       e      Perform  single  word  shell expansions, namely parameter expan-
              sion, command substitution  and  arithmetic  expansion,  on  the
              result. Such expansions can be nested but too deep recursion may
              have unpredictable effects.

## `f`

       f      Split the result of the expansion at newlines. This is a  short-
              hand for `ps:\n:'.

## `F`

       F      Join  the words of arrays together using newline as a separator.
              This is a shorthand for `pj:\n:'.

## `g:opts:`

       g:opts:
              Process escape sequences like the echo builtin when  no  options
              are  given (g::).  With the o option, octal escapes don't take a
              leading zero.  With the c option, sequences like `^X'  are  also
              processed.   With  the  e  option,  processes `\M-t' and similar
              sequences like the print builtin.  With both  of  the  o  and  e
              options,  behaves  like the print builtin except that in none of
              these modes is `\c' interpreted.

## `i`

       i      Sort case-insensitively.  May be combined with `n' or `O'.

## `k`

       k      If name refers to an  associative  array,  substitute  the  keys
              (element  names)  rather  than the values of the elements.  Used
              with subscripts (including ordinary arrays),  force  indices  or
              keys to be substituted even if the subscript form refers to val-
              ues.  However, this flag may  not  be  combined  with  subscript
              ranges.   With  the KSH_ARRAYS option a subscript `[*]' or `[@]'
              is needed to operate on the whole array, as usual.

## `L` (小文字)

       L      Convert all letters in the result to lower case.

## `n`

       n      Sort decimal integers numerically; if the first differing  char-
              acters  of  two test strings are not digits, sorting is lexical.
              Integers with more initial zeroes are sorted before  those  with
              fewer  or  none.   Hence  the  array `foo1 foo02 foo2 foo3 foo20
              foo23' is sorted into the order shown.  May be combined with `i'
              or `O'.

## `o`

       o      Sort  the resulting words in ascending order; if this appears on
              its own the sorting is lexical and  case-sensitive  (unless  the
              locale renders it case-insensitive).  Sorting in ascending order
              is the default for other forms of sorting, so this is ignored if
              combined with `a', `i' or `n'.

## `O`

       O      Sort  the  resulting words in descending order; `O' without `a',
              `i' or `n' sorts in reverse lexical order.  May be combined with
              `a', `i' or `n' to reverse the order of sorting.

## `P`

       P      This forces the value of the parameter name to be interpreted as
              a further parameter name, whose value will be used where  appro-
              priate.   Note  that flags set with one of the typeset family of
              commands (in particular case transformations) are not applied to
              the value of name used in this fashion.

              If  used  with  a  nested parameter or command substitution, the
              result of that will be taken as a parameter  name  in  the  same
              way.   For  example,  if  you  have `foo=bar' and `bar=baz', the
              strings ${(P)foo}, ${(P)${foo}}, and ${(P)$(echo bar)}  will  be
              expanded to `baz'.

              Likewise, if the reference is itself nested, the expression with
              the flag is treated as if  it  were  directly  replaced  by  the
              parameter name.  It is an error if this nested substitution pro-
              duces an array  with  more  than  one  word.   For  example,  if
              `name=assoc'  where the parameter assoc is an associative array,
              then `${${(P)name}[elt]}' refers to the element of the  associa-
              tive subscripted `elt'.

## `q`

       q      Quote  characters that are special to the shell in the resulting
              words with backslashes; unprintable or  invalid  characters  are
              quoted  using  the  $'\NNN'  form, with separate quotes for each
              octet.

              If this flag is given twice, the resulting words are  quoted  in
              single  quotes  and  if  it  is given three times, the words are
              quoted in double quotes; in these forms no special  handling  of
              unprintable  or invalid characters is attempted.  If the flag is
              given four times, the words are quoted in single quotes preceded
              by  a  $.  Note that in all three of these forms quoting is done
              unconditionally, even if  this  does  not  change  the  way  the
              resulting string would be interpreted by the shell.

              If a q- is given (only a single q may appear), a minimal form of
              single quoting is used that only quotes the string if needed  to
              protect  special characters.  Typically this form gives the most
              readable output.

              If a q+ is given, an extended form of  minmal  quoting  is  used
              that  causes unprintable characters to be rendered using $'...'.
              This quoting is similar to that used by the output of values  by
              the typeset family of commands.

## `Q`

       Q      Remove one level of quotes from the resulting words.

## `t`

       t      Use  a  string  describing  the  type of the parameter where the
              value of the parameter would usually appear.  This  string  con-
              sists  of keywords separated by hyphens (`-'). The first keyword
              in the string  describes  the  main  type,  it  can  be  one  of
              `scalar',  `array',  `integer',  `float'  or  `association'. The
              other keywords describe the type in more detail:

              local  for local parameters

              left   for left justified parameters

              right_blanks
                     for right justified parameters with leading blanks

              right_zeros
                     for right justified parameters with leading zeros

              lower  for parameters whose value is converted to all lower case
                     when it is expanded

              upper  for parameters whose value is converted to all upper case
                     when it is expanded

              readonly
                     for readonly parameters

              tag    for tagged parameters

              export for exported parameters

              unique for arrays which keep only the first occurrence of dupli-
                     cated values

              hide   for parameters with the `hide' flag

              hideval
                     for parameters with the `hideval' flag

              special
                     for special parameters defined by the shell

## `u`

       u      Expand only the first occurrence of each unique word.

## `U`

       U      Convert all letters in the result to upper case.

## `v`

       v      Used  with k, substitute (as two consecutive words) both the key
              and the value of each associative array element.  Used with sub-
              scripts,  force  values  to be substituted even if the subscript
              form refers to indices or keys.

## `V`

       V      Make any special characters in the resulting words visible.

## `w`

       w      With ${#name}, count words in arrays or strings; the s flag  may
              be used to set a word delimiter.

## `W`

       W      Similar  to  w  with  the  difference  that  empty words between
              repeated delimiters are also counted.

## `X`

       X      With this flag, parsing errors occurring with the  Q,  e  and  #
              flags  or  the  pattern matching forms such as `${name#pattern}'
              are reported.  Without the flag, errors are silently ignored.

## `z` (単語分割)

Split the result of the expansion into words using shell parsing to  find  the words,
i.e. taking into account any quoting in the value.

Comments are  not  treated  specially  but  as  ordinary strings,
similar to interactive shells with the INTERACTIVE_COMMENTS option unset
(however, see the Z flag  below  for  related options)

Note  that  this  is  done  very late, even later than the `(s)` flag.
So to access single words in the result use nested  expansions as in `${${(z)foo}[2]}`.

Likewise, to remove the quotes in the resulting words use `${(Q)${(z)foo}}`.

## `0`

       0      Split the result of the expansion on  null  bytes.   This  is  a
              shorthand for `ps:\0:'.

       The following flags (except p) are followed by one or more arguments as
       shown.  Any character, or the matching pairs `(...)', `{...}', `[...]',
       or  `<...>',  may  be  used in place of a colon as delimiters, but note
       that when a flag takes more than one argument, a matched pair of delim-
       iters must surround each argument.

## `p`

       p      Recognize  the  same  escape  sequences  as the print builtin in
              string arguments to any of the flags described below that follow
              this argument.

              Alternatively,  with  this option string arguments may be in the
              form $var in which case the value of  the  variable  is  substi-
              tuted.   Note  this form is strict; the string argument does not
              undergo general parameter expansion.

              For example,

                     sep=:
                     val=a:b:c
                     print ${(ps.$sep.)val}

              splits the variable on a :.

## `~`

       ~      Strings inserted into the expansion by any of  the  flags  below
              are to be treated as patterns.  This applies to the string argu-
              ments of flags that follow ~ within the same set of parentheses.
              Compare with ~ outside parentheses, which forces the entire sub-
              stituted string to be treated as a pattern.  Hence, for example,

                     [[ "?" = ${(~j.|.)array} ]]

              treats  `|' as a pattern and succeeds if and only if $array con-
              tains the string `?' as an element.  The ~ may  be  repeated  to
              toggle  the  behaviour;  its effect only lasts to the end of the
              parenthesised group.

## `j:string:`

       j:string:
              Join the words of arrays together using string as  a  separator.
              Note  that  this  occurs before field splitting by the s:string:
              flag or the SH_WORD_SPLIT option.

## `l:expr::string1::string2:`

              Pad the resulting words on the left.  Each word  will  be  trun-
              cated if required and placed in a field expr characters wide.

              The arguments :string1: and :string2: are optional; neither, the
              first, or both may be given.  Note that the same pairs of delim-
              iters  must  be used for each of the three arguments.  The space
              to the left will be filled with string1 (concatenated  as  often
              as  needed)  or spaces if string1 is not given.  If both string1
              and string2 are given, string2 is inserted once directly to  the
              left  of  each  word,  truncated if necessary, before string1 is
              used to produce any remaining padding.

              If either of string1 or string2 is present but empty, i.e. there
              are  two  delimiters together at that point, the first character
              of $IFS is used instead.

              If the MULTIBYTE option is in effect, the flag  m  may  also  be
              given,  in which case widths will be used for the calculation of
              padding; otherwise individual multibyte characters  are  treated
              as occupying one unit of width.

              If  the  MULTIBYTE  option  is  not  in effect, each byte in the
              string is treated as occupying one unit of width.

              Control characters are always assumed to be one unit wide;  this
              allows  the  mechanism  to be used for generating repetitions of
              control characters.

## `m`

       m      Only useful together with one of the flags l or r or with the  #
              length operator when the MULTIBYTE option is in effect.  Use the
              character width reported by the system in calculating  how  much
              of  the  string it occupies or the overall length of the string.
              Most printable characters have a width of one unit, however cer-
              tain  Asian character sets and certain special effects use wider
              characters; combining characters have zero width.  Non-printable
              characters are arbitrarily counted as zero width; how they would
              actually be displayed will vary.

              If the m is repeated, the character either counts  zero  (if  it
              has zero width), else one.  For printable character strings this
              has the effect of counting the number of glyphs  (visibly  sepa-
              rate characters), except for the case where combining characters
              themselves have non-zero width (true in certain alphabets).

## `r:expr::string1::string2:`

       r:expr::string1::string2:
              As l, but pad the words on the right and insert string2  immedi-
              ately to the right of the string to be padded.

              Left  and  right padding may be used together.  In this case the
              strategy is to apply left padding to the  first  half  width  of
              each  of  the  resulting  words, and right padding to the second
              half.  If the string to be padded has odd width the  extra  pad-
              ding is applied on the left.

## `s:string:`

       s:string:
              Force  field  splitting  at  the  separator string.  Note that a
              string of two or more characters means that  all  of  them  must
              match  in  sequence;  this  differs from the treatment of two or
              more characters in the IFS parameter.  See also the =  flag  and
              the  SH_WORD_SPLIT option.  An empty string may also be given in
              which case every character will be a separate element.

              For historical reasons, the usual  behaviour  that  empty  array
              elements  are  retained  inside  double  quotes  is disabled for
              arrays generated by splitting; hence the following:

                     line="one::three"
                     print -l "${(s.:.)line}"

              produces two lines of output for one and three  and  elides  the
              empty  field.  To override this behaviour, supply the `(@)' flag
              as well, i.e.  "${(@s.:.)line}".

## `Z:opts:`

       Z:opts:
              As z but takes a combination of option letters between a follow-
              ing pair of delimiter characters.  With no options the effect is
              identical to z.  (Z+c+) causes comments to be parsed as a string
              and retained; any field in the resulting array beginning with an
              unquoted comment character is a comment.  (Z+C+) causes comments
              to  be  parsed  and removed.  The rule for comments is standard:
              anything between a word starting with  the  third  character  of
              $HISTCHARS,  default  #,  up  to  the next newline is a comment.
              (Z+n+) causes unquoted newlines to be treated as ordinary white-
              space,  else  they  are treated as if they are shell code delim-
              iters and converted to semicolons.  Options are combined  within
              the same set of delimiters, e.g. (Z+Cn+).

## `_:flags:`

       _:flags:
              The  underscore (_) flag is reserved for future use.  As of this
              revision of zsh, there are no valid flags; anything following an
              underscore,  other  than an empty pair of delimiters, is treated
              as an error, and the flag itself has no effect.

       The following flags are meaningful with the  ${...#...}  or  ${...%...}
       forms.  The S and I flags may also be used with the ${.../...} forms.

## `S` (部分文字列検索)

       S      Search  substrings  as  well as beginnings or ends; with # start
              from the beginning and with % start from the end of the  string.
              With  substitution  via  ${.../...}  or  ${...//...},  specifies
              non-greedy matching, i.e. that the shortest instead of the long-
              est match should be replaced.

## `I:expr:`

       I:expr:
              Search  the  exprth  match  (where  expr evaluates to a number).
              This only applies when searching for substrings, either with the
              S  flag,  or  with  ${.../...} (only the exprth match is substi-
              tuted) or ${...//...} (all matches from the exprth on  are  sub-
              stituted).  The default is to take the first match.

              The  exprth  match  is  counted such that there is either one or
              zero matches from each starting position in the string, although
              for  global  substitution  matches overlapping previous replace-
              ments are ignored.  With the ${...%...} and  ${...%%...}  forms,
              the starting position for the match moves backwards from the end
              as the index increases, while with the other forms it moves for-
              ward from the start.

              Hence with the string
                     which switch is the right switch for Ipswich?
              substitutions  of  the form ${(SI:N:)string#w*ch} as N increases
              from 1 will match  and  remove  `which',  `witch',  `witch'  and
              `wich';  the form using `##' will match and remove `which switch
              is the right switch for Ipswich', `witch is the right switch for
              Ipswich',  `witch  for  Ipswich'  and `wich'. The form using `%'
              will remove the same matches as for `#', but in  reverse  order,
              and the form using `%%' will remove the same matches as for `##'
              in reverse order.

## `B`

       B      Include the index of the beginning of the match in the result.

## `E`

       E      Include the index one character past the end of the match in the
              result  (note  this is inconsistent with other uses of parameter
              index).

## `M`

       M      Include the matched portion in the result.

## `N`

       N      Include the length of the match in the result.

## `R`

       R      Include the unmatched portion in the result (the Rest).
