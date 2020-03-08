# zshmisc: PRECOMMAND MODIFIERS

 A simple command may be preceded by a precommand modifier,  
 which  will alter  how  the  command  is  interpreted.
 These  modifiers are shell builtin commands with the exception of nocorrect which  is  a  reserved word.

## `-`

- The  command  is  executed  with  a ``-'` prepended to its `argv[0]` string.

## builtin

- The command word is taken to be the name of a  builtin  command, rather than a shell function or external command.

## command [ -pvV ]

- The command word is taken to be the name of an external command, rather than a shell function or builtin.   
- If the POSIX_BUILTINS option  is  set, builtins will also be executed but certain special properties of them are suppressed. 
- The  `-p`  flag  causes  a default  path  to be searched instead of that in `$path`. 
- With the `-v` flag, command is similar to whence 
- and with `-V`, it is equivalent to whence `-v`.

## exec [ -cl ] [ -a argv0 ]

- The  following  command  together  with  any arguments is run in place of the current process, rather than as a sub-process.  
- The shell does not fork and is replaced.  
- The shell does not invoke TRAPEXIT, nor does it source zlogout  files.   
- The  options  are provided for compatibility with other shells.

- The `-c` option clears the environment.

- The  `-l`  option  is  equivalent to the `-` precommand modifier, to treat the replacement command as a login shell; 
- the  command  is executed  with  a  `-` prepended to its `argv[0]` string.  
- This flag has no effect if used together with the `-a` option.

- The `-a` option is used to specify explicitly the  `argv[0]`  string (the  name  of  the command as seen by the process itself) to be used by the replacement command 
- and is  directly  equivalent  to setting a value for the ARGV0 environment variable.

## nocorrect

- Spelling  correction is not done on any of the words.
- This must appear before any other precommand modifier,  as  it  is  interpreted  immediately,  before  any  parsing  is  done.  
- It has no effect in non-interactive shells.

## noglob Filename

- generation (globbing) is not performed on  any  of  the words.
