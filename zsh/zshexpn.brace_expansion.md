# BRACE EXPANSION

A  string  of the form `foo{xx,yy,zz}bar` is expanded to the individual
words `fooxxbar`, `fooyybar` and `foozzbar`.   Left-to-right  order  is
preserved.   This  construct  may  be  nested.  Commas may be quoted in
order to include them literally in a word.

An expression of the form `{n1..n2}`, where n1 and n2 are integers,  is
expanded to every number between n1 and n2 inclusive.  If either number
begins with a zero, all the resulting numbers will be padded with lead-
ing  zeroes to that minimum width, but for negative numbers the - char-
acter is also included in the width.  If the numbers are in  decreasing
order the resulting sequence will also be in decreasing order.

An  expression  of  the  form  `{n1..n2..n3}`, where n1, n2, and n3 are
integers, is expanded as above, but only  every  n3th  number  starting
from n1 is output.  If n3 is negative the numbers are output in reverse
order, this is slightly different from simply swapping n1 and n2 in the
case  that  the  step n3 doesn't evenly divide the range.  Zero padding
can be specified in any of the three  numbers,  specifying  it  in  the
third  can  be  useful to pad for example `{-99..100..01}` which is not
possible to specify by putting a 0 on either of the first  two  numbers
(i.e. pad to two characters).

An  expression of the form `{c1..c2}`, where c1 and c2 are single char-
acters (which may be multibyte characters), is expanded to every  char-
acter in the range from c1 to c2 in whatever character sequence is used
internally.  For characters with code points below 128 this is US ASCII
(this is the only case most users will need).  If any intervening char-
acter is not printable, appropriate quotation  is  used  to  render  it
printable.   If  the  character  sequence is reversed, the output is in
reverse order, e.g. `{d..a}` is substituted as `d c b a`.

If a brace expression matches none of  the  above  forms,  it  is  left
unchanged,  unless  the  option  BRACE_CCL  (an abbreviation for `brace character class`) is set.  
In that case, it is expanded to  a  list  of
the  individual  characters between the braces sorted into the order of
the characters in the ASCII character set (multibyte characters are not
currently  handled).   The  syntax  is similar to a [...] expression in
filename generation: `-` is treated specially  to  denote  a  range  of
characters,  but `^` or `!` as the first character is treated normally.
For example, `{abcdef0-9}` expands to 16 words `0 1 2 3 4 5 6 7 8 9 a  b c d e f`.

Note  that  brace  expansion  is not part of filename generation (globbing);
an expression such as */{foo,bar} is  split  into  two  separate
words  */foo and */bar before filename generation takes place.  In par-
ticular, note that this is liable to produce  a  `no  match'  error  if
either  of the two expressions does not match; this is to be contrasted
with */(foo|bar), which is treated as a single  pattern  but  otherwise
has similar effects.

To  combine brace expansion with array expansion, see the ${^spec} form
described in the section Parameter Expansion above.
