# zshexpan: PARAMETER EXPANSION

The  character `$' is used to introduce parameter expansions.

See [zshparam(1)](zshparam) for a description of parameters,
including arrays, associative arrays, and subscript notation to access individual array elements.

Note in particular the fact that words of unquoted parameters are not automatically split on whitespace
unless the option SH_WORD_SPLIT is set;
see references to this option below for more details.
This is an important difference from other shells.

In the expansions discussed below that require a pattern,
the form of the pattern is the same as that used for filename generation;
see the section `Filename Generation'.

Note that these patterns,
along with the replacement text of any substitutions,
are themselves subject to parameter expansion, command substitution, and arithmetic expansion.

コロン修飾子:

In addition to the following operations,
the colon modifiers described in the section `Modifiers` in the section `History Expansion` can be applied:
for example, `${i:s/foo/bar/}` performs string substitution on the expansion of parameter `$i`.

In the following descriptions, `word` refers to a single word substituted on the command line,
not necessarily a space delimited word.
With default options, after the assignments:

~~~zsh
    array=("first word" "second word")
    scalar="only word"
~~~

then `$array` substitutes two words, `first word` and `second word`,
and `$scalar` substitutes a single word `only word'.
This may be modified by explicit or implicit word-splitting, however.
The full rules are com plicated and are noted at the end.

## `${name}`

The value, if any, of the parameter name is substituted.

The braces are required if the expansion is to be followed by a letter, digit, or underscore that is not to be interpreted as part of name.

In addition,
more complicated forms of substitution usually require the braces to be present; exceptions,
which only apply if the option KSH_ARRAYS is not set, are a single subscript or any colon modifiers appearing after the name,
or any of the characters `^`, `=`, `~`, `#` or `+` appearing before the name, all of which work with or without braces.

If name is an array parameter, and the KSH_ARRAYS option is not set,
then the value of each element of name is substituted, one element per word.

Otherwise, the expansion results in one word only; with KSH_ARRAYS, this is the first element of an array.

No field splitting is done on the result unless the SH_WORD_SPLIT option is set.

See also the flags `=` and `s:string:`.

## `${+name}`

If name is the name of a set parameter `1` is substituted, otherwise `0` is substituted.

## `${name-word}`  `${name:-word}` 

       `name` あり -> `name`, なし -> `word`

If `name` is set, or in the second form is non-null, then substitute its value;
otherwise substitute word.

In the second form `name` may be omitted, in which case `word` is always substituted.

## `${name+word}`  `${name:+word}`

       `name`あり-> `word`, なし -> `空`

If `name` is set, or in the second form is non-null,
then substitute word; otherwise substitute nothing.

## `${name=word}`  `${name:=word}` `${name::=word}` 

       `name` あり -> `name,  
              なし -> 1. `空 `, 2.`word`, 3.`word`(ありでも)

In  the first form, if name is unset then set it to word;
in the second form, if name is unset or null then set it to word;
and in the third form, unconditionally set name to word.

In all forms, the value of the parameter is then substituted.

## `${name?word}` `${name:?word}`

       `name` あり -> `name,  なし -> エラー終了 

In the first form, if name is set, or in the second form if name is both set and non-null, then substitute its value;
otherwise, print word and exit from the shell.

Interactive shells instead return to the prompt.

If word is omitted, then a standard message is printed.

In any of the above expressions that test a variable and substitute an alternate word,
note that you can use standard shell quoting in the word value to selectively override the splitting done
by the SH_WORD_SPLIT option and the = flag,
but not splitting by the s:string: flag.

## サンプル

~~~zsh
#!/bin/zsh
echo "===="
echo ${1:-msg1}

echo "===="
echo ${1:+msg2}

echo "===="
V=$1; echo ${V=msg3} ; echo $V;
V=$1; echo ${V:=msg3} ; echo $V;
V=$1; echo ${V::=msg3}; echo $V;

echo "===="
echo ${1?msg4} ${1:?msg4}
~~~

引数なし:

~~~zsh
$ ~/Downloads/words.zsh
====
msg1
====

====


msg3
msg3
msg3
msg3
====
/Users/hide/Downloads/words.zsh:14: 1: msg4
~~~

引数あり:

~~~zsh
$ ~/Downloads/words.zsh MUSIC
====
MUSIC
====
msg2
====
MUSIC
MUSIC
MUSIC
MUSIC
msg3
msg3
====
MUSIC MUSIC
~~~

In the following expressions,
when name is an array and  the  substitution is not quoted,
or if the `(@)` flag or the `name[@]` syntax is used,
matching and replacement is performed on each array element separately.

## `${name#pattern}` `${name##pattern}`

If the pattern matches the beginning of the value of name,
then substitute the value of name with the matched portion deleted;
otherwise, just substitute the value of name.

In the first form, the smallest matching pattern is preferred;
in the second form, the largest matching pattern is preferred.

## `${name%pattern}` `${name%%pattern}`

If the pattern matches the end of the value of name,
then substitute the value of name with the matched portion deleted;
otherwise,  just  substitute the value of name.

In the first form, the smallest matching pattern is preferred;
in the second form, the largest matching pattern is preferred.

## `${name:#pattern}`

If the pattern matches the value of name, then substitute the empty string;
otherwise, just substitute the value of name.

If name  is  an  array the matching array elements are removed
(use the `(M)` flag to remove the non-matched elements).

## `${name:|arrayname}`

If arrayname is the name (N.B., not contents) of an array  variable,
then any elements contained in arrayname are removed from the substitution of name.

If the substitution is scalar, either because  name  is a scalar variable or the expression is quoted,
the elements of arrayname are instead tested against the  entire expression.

## `${name:*arrayname}`

Similar to the preceding substitution, but in the opposite sense,
so that entries present in both the original substitution and as elements of arrayname are retained and others removed.

## `${name:^arrayname}`  `${name:^^arrayname}`

Zips two arrays,
such that the output array is twice as long as the shortest (longest for `:^^`) of name and arrayname,
with the elements  alternatingly being picked from them.

For `:^`, if one of the input arrays is longer,
the output will stop when the end of the shorter array is reached.

Thus,

~~~zsh
a=(1 2 3 4); b=(a b); print ${a:^b}
~~~

will  output  `1 a 2 b`.

For `:^^`,
then the input is repeated until all of the longer array has been used  up
and  the  above will output `1 a 2 b 3 a 4 b`.

Either  or  both inputs may be a scalar,
they will be treated as an array of length 1 with the scalar as  the  only  element.

If either  array  is empty, the other array is output with no extra elements inserted.

Currently the following code will output `a b` and  `1`  as  two separate  elements,
which  can  be unexpected.

The second print provides a workaround which should continue to work if  this  is changed.

~~~zsh
a=(a b); b=(1 2); print -l "${a:^b}"; print -l "${${a:^b}}"
~~~

## `${name:offset}`  `${name:offset:length}`

This  syntax  gives effects similar to parameter subscripting in
the form $name[start,end], but is compatible with other  shells;
note  that  both  offset  and length are interpreted differently
from the components of a subscript.

If offset is non-negative, then if the variable name is a scalar
substitute  the  contents  starting  offset  characters from the
first character of the string, and if name is an  array  substi-
tute  elements  starting offset elements from the first element.
If length is given, substitute that many characters or elements,
otherwise the entire rest of the scalar or array.

A positive offset is always treated as the offset of a character
or element in name from the first character or  element  of  the
array  (this  is  different from native zsh subscript notation).
Hence 0 refers to the first character or element  regardless  of
the setting of the option KSH_ARRAYS.

A negative offset counts backwards from the end of the scalar or
array, so that -1 corresponds to the last character or  element, and so on.

When positive, length counts from the offset position toward the
end of the scalar or array.  When negative, length  counts  back
from  the  end.  If this results in a position smaller than off-
set, a diagnostic is printed and nothing is substituted.

The option MULTIBYTE is obeyed, i.e. the offset and length count multibyte characters where appropriate.

offset and length undergo the same set of shell substitutions as
for scalar assignment; in addition, they  are  then  subject  to
arithmetic evaluation.

Hence, for example

~~~zsh
print ${foo:3}
print ${foo: 1 + 2}
print ${foo:$(( 1 + 2))}
print ${foo:$(echo 1 + 2)}
~~~

all  have the same effect, extracting the string starting at the
character of $foo if  the  substitution  would  otherwise
return  a scalar, or the array starting at the fourth element if
$foo  would  return  an  array.   Note  that  with  the   option
KSH_ARRAYS  $foo  always returns a scalar (regardless of the use
of the offset syntax) and a form such as ${foo[*]:3} is required
to extract elements of an array named foo.

If  offset  is  negative, the - may not appear immediately after
the : as this indicates the ${name:-word} form of  substitution.
Instead,  a  space  may  be inserted before the -.  Furthermore,
neither offset nor length may begin with an alphabetic character
or  & as these are used to indicate history-style modifiers.  To
substitute a value from a variable, the recommended approach  is
to  precede it with a $ as this signifies the intention (parame-
ter substitution can easily be rendered unreadable); however, as
arithmetic  substitution  is  performed,  the  expression `${var: offs}` does work, retrieving the offset from $offs.

For further compatibility with other shells there is  a  special
case  for  array offset 0.  This usually accesses the first ele-
ment of the array.  However, if the substitution refers  to  the
positional parameter array, e.g. $@ or $*, then offset 0 instead
refers to $0, offset 1 refers to $1, and so on.  In other words,
the  positional  parameter  array  is  effectively  extended  by
prepending $0.  Hence ${*:0:1} substitutes $0 and ${*:1:1}  sub-
stitutes $1.

## `${name/pattern/repl}`   `${name//pattern/repl}`   `${name:/pattern/repl}`

Replace  the  longest possible match of pattern in the expansion
of parameter name by string repl.  The first form replaces  just
the  first  occurrence, the second form all occurrences, and the
third form replaces only if pattern matches the  entire  string.
Both pattern and repl are subject to double-quoted substitution,
so that expressions like ${name/$opat/$npat} will work, but obey
the  usual rule that pattern characters in $opat are not treated
specially unless either the option GLOB_SUBST is set,  or  $opat
is instead substituted as ${~opat}.

The pattern may begin with a `#`,
in which case the pattern must match at the start of the string, or `%`,
in which case it must match at the end of the string,
or `#%` in which case the pattern must match the entire string.

The repl  may  be  an  empty
string,  in  which  case  the final `/` may also be omitted.  To
quote the final `/` in other cases it should be  preceded  by  a
single backslash; this is not necessary if the `/` occurs inside
a substituted parameter.  Note also that the `#`,  `%`  and  `#%` are  not  active  if  they occur inside a substituted parameter, even at the start.

If, after quoting rules apply, ${name} expands to an array,  the
replacements  act  on  each element individually.  Note also the
effect of the I and S parameter expansion flags below;  however,
the flags M, R, B, E and N are not useful.

For example,

~~~zsh
foo="twinkle twinkle little star" sub="t*e" rep="spy"
print ${foo//${~sub}/$rep}
print ${(S)foo//${~sub}/$rep}
~~~

Here, the `~` ensures that the text of $sub is treated as a pat-
tern rather than a plain string.  In the first case, the longest
match for t*e is substituted and the result is `spy star`,
while in the second case, the  shortest  matches  are  taken  and  the result is `spy spy lispy star`.

## `${#spec}`

`spec` is one of the above substitutions,
substitute the length in characters of the result instead of the result itself.

If `spec` is an array expression, substitute the number of elements of the result.
This has the side-effect that joining is skipped even in quoted forms,
which may affect other sub-expressions in `spec`.

Note that `^`, `=`, and `~`, below, must appear to the left of `#` when these forms are combined.

If the option `POSIX_IDENTIFIERS` is not set, and `spec` is a simple name, then the braces are optional;
this is true even for special parameters so e.g. `$#-` and `$#*` take the length of the string `$-` and the array `$*` respectively.
If POSIX_IDENTIFIERS is set, then braces are required for the # to be treated in this fashion.

## `${^spec}`

Turn on the `RC_EXPAND_PARAM` option for the evaluation  of  spec;
if  the  `^'  is doubled, turn it off.  When this option is set,
array expansions of the form foo${xx}bar, where the parameter xx
is  set  to  (a  b  c),  are  substituted  with `fooabar foobbar
foocbar' instead of the default `fooa b  cbar'.   Note  that  an
empty array will therefore cause all arguments to be removed.

Internally, each such expansion is converted into the equivalent list  for  brace  expansion.
E.g., `${^var}` becomes `{$var[1],$var[2],...}`,
and is processed as described in the section `Brace Expansion` below:
note, however, the expansion happens immediately, with any explicit brace expansion happening later.
If word splitting is also in effect the $var[N] may
themselves be split into different list elements.

## `${=spec}`

Perform  word splitting using the rules for SH_WORD_SPLIT during
the evaluation of spec, but regardless of whether the  parameter
appears  in  double  quotes; if the `=` is doubled, turn it off.

This forces parameter expansions to be split into separate words
before  substitution, using IFS as a delimiter.  This is done by
default in most other shells.

Note that splitting is applied to word in the  assignment  forms
of  spec  before  the  assignment  to  name  is performed.  This
affects the result of array assignments with the A flag.

## `${~spec}`

Turn on the `GLOB_SUBST` option for the evaluation of spec;
if the `~` is doubled, turn it off.

When this option is set, the string resulting from the expansion will be interpreted
as  a pattern anywhere that is possible,
such as in filename expansion and filename generation and pattern-matching contexts like the
right hand side of the `=` and `!=` operators in conditions.

In nested substitutions,
note that the effect of the `~` applies to the result of the current level of substitution.
A surrounding pattern operation on the result may cancel it.
Hence, for example, if the parameter foo is set to `*`,
`${~foo//\*/*.c}` is substituted by the pattern *.c, which may be expanded by filename generation,
but `${${~foo}//\*/*.c}` substitutes to the string *.c, which will not be further expanded.

If  a ${...} type parameter expression or a $(...) type command substi-
tution is used in place of name above, it is  expanded  first  and  the
result is used as if it were the value of name.  Thus it is possible to
perform nested operations:  ${${foo#head}%tail} substitutes  the  value
of  $foo  with both `head` and `tail` deleted.  The form with $(...) is
often useful in combination with the  flags  described  next;  see  the
examples  below.   Each  name or nested ${...} in a parameter expansion
may also be followed by a subscript expression as  described  in  Array
Parameters in zshparam(1).

Note  that double quotes may appear around nested expressions, in which
case  only  the  part  inside  is  treated  as  quoted;  for   example,
${(f)"$(foo)"}  quotes  the  result  of $(foo), but the flag `(f)' (see
below) is applied using the rules for unquoted expansions.   Note  fur-
ther that quotes are themselves nested in this context; for example, in
"${(@f)"$(foo)"}", there are two sets of quotes,  one  surrounding  the
whole  expression,  the  other  (redundant)  surrounding  the $(foo) as before.
