# COMMAND SUBSTITUTION

A command enclosed in parentheses preceded by a dollar sign,
like `$(...)`, or quoted with grave accents, like ``...``, is replaced  with its  standard  output,
with any trailing newlines deleted.

If the substitution is not enclosed in double quotes, the output is  broken  into words using the IFS parameter.

The  substitution `$(cat foo)` may be replaced by the faster `$(<foo)`.

In this case foo undergoes  single  word  shell  expansions  (parameter
expansion,  command  substitution  and  arithmetic  expansion), but not
filename generation.

If the option GLOB_SUBST is set, the result  of  any  unquoted  command
substitution,  including  the  special form just mentioned, is eligible
for filename generation.
