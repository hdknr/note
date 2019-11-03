# zshexpn - zsh expansion and substitution

DESCRIPTION:

- [History Expansion](zshexpn.history_expansion.md)

This is performed only in interactive shells.

- Alias Expansion

Aliases are expanded immediately  before  the  command  line  is
parsed as explained under Aliasing in zshmisc(1).

- [Process Substitution](zshexpn.process_substitution.md)
- [Parameter Expansion](zshexpn.parameter_expansion.md)
- [Command Substitution](zshexpn.command_substitution.md)
- [Arithmetic Expansion](zshexpn.arithmetic_expansion.md)
- [Brace Expansion](zshexpn.brace_expansion.md)

These  five  are  performed  in  left-to-right fashion.  
On each argument, any of the five steps that are  needed  are  performed one  after  the  other.
Hence,  for  example, all the parts of parameter expansion are completed before command substitution is started.
After  these  expansions, all unquoted occurrences of the characters `\',`'` and `"` are removed.

- [Filename Expansion](zshexpn.filename_expansion.md)

If the `SH_FILE_EXPANSION` option is set, the order  of  expansion is  modified  for  compatibility  with sh and ksh.
In that case filename expansion is performed immediately after  alias  expan sion, preceding the set of five expansions mentioned above.

- [Filename Generation](zshexpn.filename_generation.md)

This expansion, commonly referred to as globbing, is always done last.
