# FILENAME EXPANSION

       Each word is checked to see if it begins with an unquoted `~'.   If  it
       does,  then the word up to a `/', or the end of the word if there is no
       `/', is checked to see if it can be substituted  in  one  of  the  ways
       described  here.   If  so,  then  the  `~'  and the checked portion are
       replaced with the appropriate substitute value.

       A `~' by itself is replaced by the value of $HOME.  A `~' followed by a
       `+'  or  a  `-'  is  replaced by current or previous working directory,
       respectively.

       A `~' followed by a number is replaced by the directory at  that  posi-
       tion  in  the directory stack.  `~0' is equivalent to `~+', and `~1' is
       the top of the stack.  `~+' followed by a number  is  replaced  by  the
       directory at that position in the directory stack.  `~+0' is equivalent
       to `~+', and `~+1' is the top of the stack.  `~-' followed by a  number
       is replaced by the directory that many positions from the bottom of the
       stack.  `~-0' is the bottom  of  the  stack.   The  PUSHD_MINUS  option
       exchanges  the  effects  of  `~+' and `~-' where they are followed by a
       number.


## Dynamic named directories

       If the  function  zsh_directory_name  exists,  or  the  shell  variable
       zsh_directory_name_functions  exists  and contains an array of function
       names, then the functions are used to implement dynamic directory  nam-
       ing.   The  functions are tried in order until one returns status zero,
       so it is important that functions test whether they can handle the case
       in question and return an appropriate status.

       A  `~'  followed  by  a  string  namstr  in unquoted square brackets is
       treated specially as a dynamic directory name.   Note  that  the  first
       unquoted  closing  square  bracket always terminates namstr.  The shell
       function is passed two arguments: the string n (for name)  and  namstr.
       It  should  either set the array reply to a single element which is the
       directory corresponding to the name and return status  zero  (executing
       an  assignment  as  the  last  statement  is usually sufficient), or it
       should return status non-zero.  In the former case the element of reply
       is used as the directory; in the latter case the substitution is deemed
       to have failed.  If all functions fail and the option NOMATCH  is  set,
       an error results.

       The  functions defined as above are also used to see if a directory can
       be turned into a name, for example when printing the directory stack or
       when expanding %~ in prompts.  In this case each function is passed two
       arguments: the string d (for directory) and the candidate  for  dynamic
       naming.   The  function  should  either  return non-zero status, if the
       directory cannot be named by the function, or it should set  the  array
       reply to consist of two elements: the first is the dynamic name for the
       directory (as would appear within `~[...]'), and the second is the pre-
       fix  length of the directory to be replaced.  For example, if the trial
       directory  is   /home/myname/src/zsh   and   the   dynamic   name   for
       /home/myname/src (which has 16 characters) is s, then the function sets

              reply=(s 16)

       The directory name so returned is compared with possible  static  names
       for  parts of the directory path, as described below; it is used if the
       prefix length matched (16 in the example) is longer than  that  matched
       by any static name.

       It  is not a requirement that a function implements both n and d calls;
       for example, it might be  appropriate  for  certain  dynamic  forms  of
       expansion  not  to  be contracted to names.  In that case any call with
       the first argument d should cause a non-zero status to be returned.

       The completion system calls `zsh_directory_name c' followed by  equiva-
       lent calls to elements of the array zsh_directory_name_functions, if it
       exists, in order to complete dynamic names for directories.   The  code
       for this should be as for any other completion function as described in
       zshcompsys(1).

       As a working example, here is a function that expands any dynamic names
       beginning  with  the string p: to directories below /home/pws/perforce.
       In this simple case a static name for the directory would  be  just  as
       effective.

~~~zsh
              zsh_directory_name() {
                emulate -L zsh
                setopt extendedglob
                local -a match mbegin mend
                if [[ $1 = d ]]; then
                  # turn the directory into a name
                  if [[ $2 = (#b)(/home/pws/perforce/)([^/]##)* ]]; then
                    typeset -ga reply
                    reply=(p:$match[2] $(( ${#match[1]} + ${#match[2]} )) )
                  else
                    return 1
                  fi
                elif [[ $1 = n ]]; then
                  # turn the name into a directory
                  [[ $2 != (#b)p:(?*) ]] && return 1
                  typeset -ga reply
                  reply=(/home/pws/perforce/$match[1])
                elif [[ $1 = c ]]; then
                  # complete names
                  local expl
                  local -a dirs
                  dirs=(/home/pws/perforce/*(/:t))
                  dirs=(p:${^dirs})
                  _wanted dynamic-dirs expl 'dynamic directory' compadd -S\] -a dirs
                  return
                else
                  return 1
                fi
                return 0
              }
~~~

## Static named directories

       A `~' followed by anything not already covered consisting of any number
       of alphanumeric characters or underscore (`_'), hyphen  (`-'),  or  dot
       (`.')  is  looked up as a named directory, and replaced by the value of
       that named directory if found.  Named directories  are  typically  home
       directories  for  users on the system.  They may also be defined if the
       text after the `~' is the name of a string shell parameter whose  value
       begins with a `/'.  Note that trailing slashes will be removed from the
       path to the directory (though the original parameter is not  modified).

       It  is  also  possible to define directory names using the -d option to
       the hash builtin.

       When the shell prints a path (e.g. when expanding %~ in prompts or when
       printing  the  directory stack), the path is checked to see if it has a
       named directory as its prefix.  If  so,  then  the  prefix  portion  is
       replaced with a `~' followed by the name of the directory.  The shorter
       of the two ways of referring to the directory is used, i.e. either  the
       directory  name or the full path; the name is used if they are the same
       length.  The parameters $PWD and $OLDPWD are never abbreviated in  this
       fashion.

## `=` expansion

       If a word begins with an unquoted `=' and the EQUALS option is set, the
       remainder of the word is taken as the name of a command.  If a  command
       exists  by  that name, the word is replaced by the full pathname of the
       command.


## Notes

       Filename expansion is performed on the right hand side of  a  parameter
       assignment,  including  those  appearing  after commands of the typeset
       family.  In this case, the  right  hand  side  will  be  treated  as  a
       colon-separated list in the manner of the PATH parameter, so that a `~'
       or an `=' following a `:' is eligible for expansion.  All  such  behav-
       iour  can be disabled by quoting the `~', the `=', or the whole expres-
       sion (but not simply the colon); the EQUALS option is also respected.

       If the option MAGIC_EQUAL_SUBST is set, any unquoted shell argument  in
       the form `identifier=expression' becomes eligible for file expansion as
       described in the  previous  paragraph.   Quoting  the  first  `='  also
       inhibits this.
