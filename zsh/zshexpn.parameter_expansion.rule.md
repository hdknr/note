# Rules

       Here is a summary of the rules  for  substitution;  this  assumes  that
       braces are present around the substitution, i.e. ${...}.  Some particu-
       lar examples are given below.  Note  that  the  Zsh  Development  Group
       accepts  no  responsibility for any brain damage which may occur during
       the reading of the following rules.

## 1. Nested substitution

              If multiple nested ${...} forms  are  present,  substitution  is
              performed  from the inside outwards.  At each level, the substi-
              tution takes account of whether the current value is a scalar or
              an  array,  whether  the whole substitution is in double quotes,
              and what flags are supplied to the current  level  of  substitu-
              tion,  just  as  if  the nested substitution were the outermost.
              The flags are not propagated up to enclosing substitutions;  the
              nested  substitution  will return either a scalar or an array as
              determined by the flags, possibly adjusted for quoting.  All the
              following  steps  take  place  where applicable at all levels of
              substitution.

              Note that, unless the `(P)' flag is present, the flags  and  any
              subscripts  apply  directly to the value of the nested substitu-
              tion; for example, the expansion ${${foo}} behaves  exactly  the
              same as ${foo}.  When the `(P)' flag is present in a nested sub-
              stitution, the other substitution rules are applied to the value
              before  it  is interpreted as a name, so ${${(P)foo}} may differ
              from ${(P)foo}.

              At each nested level  of  substitution,  the  substituted  words
              undergo all forms of single-word substitution (i.e. not filename
              generation), including command substitution,  arithmetic  expan-
              sion  and  filename expansion (i.e. leading ~ and =).  Thus, for
              example, ${${:-=cat}:h} expands to the directory where  the  cat
              program resides.  (Explanation: the internal substitution has no
              parameter but a default value =cat, which is expanded  by  file-
              name  expansion  to  a  full  path;  the outer substitution then
              applies the modifier :h and takes  the  directory  part  of  the
              path.)

## 2. Internal parameter flags

              Any  parameter  flags  set  by one of the typeset family of com-
              mands, in particular the -L, -R, -Z, -u and -l options for  pad-
              ding  and  capitalization, are applied directly to the parameter
              value.  Note these flags are options to the command, e.g. `type-
              set  -Z'; they are not the same as the flags used within parame-
              ter substitutions.

              At the outermost level of substitution, the `(P)' flag (rule 4.)
              ignores  these  transformations and uses the unmodified value of
              the parameter as the name to be replaced.  This is  usually  the
              desired  behavior  because  padding may make the value syntacti-
              cally illegal as a parameter name, but if capitalization changes
              are desired, use the ${${(P)foo}} form (rule 25.).

## 3. Parameter subscripting

              If the value is a raw parameter reference with a subscript, such
              as ${var[3]}, the effect of subscripting is applied directly  to
              the  parameter.   Subscripts are evaluated left to right; subse-
              quent subscripts apply to the scalar or array value  yielded  by
              the  previous  subscript.  Thus if var is an array, ${var[1][2]}
              is the second character of the first word, but ${var[2,4][2]} is
              the entire third word (the second word of the range of words two
              through four of the original array).  Any number  of  subscripts
              may  appear.   Flags  such  as  `(k)'  and `(v)' which alter the
              result of subscripting are applied.

## 4. Parameter name replacement

              At the outermost level  of  nesting  only,  the  `(P)'  flag  is
              applied.   This  treats  the  value  so  far as a parameter name
              (which may include a subscript  expression)  and  replaces  that
              with  the corresponding value.  This replacement occurs later if
              the `(P)' flag appears in a nested substitution.

              If the value so far names a parameter that  has  internal  flags
              (rule  2.),  those  internal  flags are applied to the new value
              after replacement.

## 5. Double-quoted joining

              If the value after this process is an array, and  the  substitu-
              tion  appears  in double quotes, and neither an `(@)' flag nor a
              `#' length operator is present at the current level, then  words
              of  the value are joined with the first character of the parame-
              ter $IFS, by default a space, between  each  word  (single  word
              arrays are not modified).  If the `(j)' flag is present, that is
              used for joining instead of $IFS.

## 6. Nested subscripting

              Any remaining subscripts (i.e. of  a  nested  substitution)  are
              evaluated  at this point, based on whether the value is an array
              or a scalar.  As with 3., multiple subscripts can appear.   Note
              that  ${foo[2,4][2]} is thus equivalent to ${${foo[2,4]}[2]} and
              also to "${${(@)foo[2,4]}[2]}" (the nested substitution  returns
              an  array  in  both  cases), but not to "${${foo[2,4]}[2]}" (the
              nested substitution returns a scalar because of the quotes).

## 7. Modifiers

              Any modifiers, as specified by a trailing `#', `%', `/'  (possi-
              bly  doubled)  or  by a set of modifiers of the form `:...' (see
              the section `Modifiers' in the section `History Expansion'), are
              applied to the words of the value at this level.

## 8. Character evaluation
              Any  `(#)' flag is applied, evaluating the result so far numeri-
              cally as a character.

## 9. Length

              Any initial `#' modifier, i.e. in the form ${#var}, is  used  to
              evaluate the length of the expression so far.

## 10. Forced joining

              If  the  `(j)'  flag is present, or no `(j)' flag is present but
              the string is to be split as given by rule 11., and joining  did
              not  take  place  at  rule 5., any words in the value are joined
              together using the given string or the first character  of  $IFS
              if  none.  Note that the `(F)' flag implicitly supplies a string
              for joining in this manner.

## 11. Simple word splitting

              If one of the `(s)' or `(f)' flags are present, or the `=' spec-
              ifier  was  present  (e.g. ${=var}), the word is split on occur-
              rences of the specified string, or (for = with  neither  of  the
              two flags present) any of the characters in $IFS.

              If  no `(s)', `(f)' or `=' was given, but the word is not quoted
              and the option SH_WORD_SPLIT is set, the word is split on occur-
              rences  of  any of the characters in $IFS.  Note this step, too,
              takes place at all levels of a nested substitution.

## 12. Case modification

              Any case modification from one of  the  flags  `(L)',  `(U)'  or
              `(C)' is applied.

## 13. Escape sequence replacement

              First  any  replacements from the `(g)' flag are performed, then
              any prompt-style formatting from the `(%)' family  of  flags  is
              applied.

## 14. Quote application

              Any quoting or unquoting using `(q)' and `(Q)' and related flags
              is applied.

## 15. Directory naming

              Any directory name substitution using `(D)' flag is applied.

## 16. Visibility enhancement

              Any modifications to make characters  visible  using  the  `(V)'
              flag are applied.

## 17. Lexical word splitting

              If  the  '(z)'  flag  or  one  of the forms of the '(Z)' flag is
              present, the word is split as if it were a shell  command  line,
              so  that  quotation  marks  and other metacharacters are used to
              decide what constitutes a word.  Note this form of splitting  is
              entirely  distinct  from that described by rule 11.: it does not
              use $IFS, and does not cause forced joining.

## 18. Uniqueness

              If the result is an array and the `(u)' flag was present, dupli-
              cate elements are removed from the array.

## 19. Ordering

              If  the  result  is still an array and one of the `(o)' or `(O)'
              flags was present, the array is reordered.

## 20. RC_EXPAND_PARAM

              At this point the decision is made whether any  resulting  array
              elements  are to be combined element by element with surrounding
              text, as given by either the RC_EXPAND_PARAM option or  the  `^'
              flag.

## 21. Re-evaluation

              Any  `(e)'  flag  is  applied  to  the  value,  forcing it to be
              re-examined for new parameter substitutions, but also  for  com-
              mand and arithmetic substitutions.

## 22. Padding

              Any padding of the value by the `(l.fill.)' or `(r.fill.)' flags
              is applied.

## 23. Semantic joining

              In contexts where expansion semantics requires a single word  to
              result,  all  words are rejoined with the first character of IFS
              between.  So in `${(P)${(f)lines}}' the  value  of  ${lines}  is
              split  at  newlines,  but  then  must be joined again before the
              `(P)' flag can be applied.

              If a single word is not required, this rule is skipped.

## 24. Empty argument removal

              If the substitution  does  not  appear  in  double  quotes,  any
              resulting zero-length argument, whether from a scalar or an ele-
              ment of an array, is elided from the list of arguments  inserted
              into the command line.

              Strictly speaking, the removal happens later as the same happens
              with other forms of substitution; the point to note here is sim-
              ply  that it occurs after any of the above parameter operations.

## 25. Nested parameter name replacement

              If the `(P)' flag is present and rule 4. has  not  applied,  the
              value so far is treated as a parameter name (which may include a
              subscript expression) and replaced with the corresponding value,
              with internal flags (rule 2.) applied to the new value.