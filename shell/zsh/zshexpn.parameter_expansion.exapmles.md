# Examples

The  flag  f  is  useful  to split a double-quoted substitution line by
line.  For example, ${(f)"$(<file)"} substitutes the contents  of  file
divided  so  that each line is an element of the resulting array.  Com-
pare this with the effect of $(<file) alone, which divides the file  up
by words, or the same inside double quotes, which makes the entire con-
tent of the file a single string.

The following illustrates the rules for  nested  parameter  expansions.
Suppose that $foo contains the array (bar baz):

## "${(@)${foo}[1]}"

This  produces  the  result  b.   First,  the inner substitution
"${foo}", which has no array (@) flag, produces  a  single  word
result "bar baz".  The outer substitution "${(@)...[1]}" detects
that this is a scalar, so that (despite the `(@)' flag) the sub-
script picks the first character.

## "${${(@)foo}[1]}"

This produces the result `bar'.  In this case, the inner substi-
tution "${(@)foo}" produces the array `(bar  baz)'.   The  outer
substitution "${...[1]}" detects that this is an array and picks
the first word.  This is similar to the simple case "${foo[1]}".

As an example of the rules for word splitting and joining, suppose $foo
contains the array `(ax1 bx1)'.  Then

## ${(s/x/)foo}


produces the words `a`, `1 b` and `1`.

## ${(j/x/s/x/)foo}

produces `a`, `1`, `b` and `1`.

## ${(s/x/)foo%%1*}

produces `a` and ` b` (note the extra space).   As  substitution
occurs  before either joining or splitting, the operation  first
generates the modified array (ax bx), which is  joined  to  give
"ax  bx",  and  then  split to give `a`, ` b` and ``.  

The final empty string will then be elided, as it is not in double quotes.
