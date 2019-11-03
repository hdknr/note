# PROCESS SUBSTITUTION

Each part  of  a  command  argument  that  takes  the  form  `<(list)`,
`>(list)` or `=(list)` is subject to process substitution.  The expres-
sion may be preceded or followed by other strings except that, to  pre-
vent  clashes  with  commonly  occurring strings and patterns, the last
form must occur at the start of a command argument, and the  forms  are
only  expanded  when  first  parsing  command  or assignment arguments.

Process substitutions may be used following redirection  operators;  in
this case, the substitution must appear with no trailing string.

Note  that  `<<(list)`  is not a special syntax; it is equivalent to `<<(list)`,
redirecting standard input from the result of process substitution.
Hence  all  the  following documentation applies.
The second form (with the space) is recommended for clarity.

In the case of the < or > forms, the shell runs the commands in list as
a  subprocess of the job executing the shell command line.  If the sys-
tem supports the /dev/fd mechanism, the command argument is the name of
the  device  file corresponding to a file descriptor; otherwise, if the
system supports named pipes (FIFOs), the command  argument  will  be  a
named  pipe.   If the form with > is selected then writing on this spe-
cial file will provide input for list.  If < is  used,  then  the  file
passed  as  an  argument  will  be  connected to the output of the list
process.  For example,

~~~zsh
paste <(cut -f1 file1) <(cut -f3 file2) |
tee >(process1) >(process2) >/dev/null
~~~

cuts fields 1 and 3 from the files file1 and file2 respectively, pastes
the  results  together,  and  sends  it  to  the processes process1 and
process2.

If =(...) is used instead of <(...), then the file passed as  an  argu-
ment  will be the name of a temporary file containing the output of the
list process.  This may be used instead of the <  form  for  a  program
that expects to lseek (see lseek(2)) on the input file.

There is an optimisation for substitutions of the form =(<<<arg), where
arg is a single-word argument to the here-string redirection <<<.  This
form produces a file name containing the value of arg after any substi-
tutions have been performed.  This is handled entirely within the  cur-
rent  shell.   This  is  effectively  the  reverse  of the special form
$(<arg) which treats arg as a file name and replaces it with the file's
contents.

The = form is useful as both the /dev/fd and the named pipe implementa-
tion of <(...) have drawbacks.  In the former case, some programmes may
automatically  close  the  file descriptor in question before examining
the file on the command line, particularly if  this  is  necessary  for
security  reasons such as when the programme is running setuid.  In the
second case, if the programme does not actually open the file, the sub-
shell  attempting  to read from or write to the pipe will (in a typical
implementation, different operating systems may have  different  behav-
iour)  block for ever and have to be killed explicitly.  In both cases,
the shell actually supplies the information using a pipe, so that  pro-
grammes  that expect to lseek (see lseek(2)) on the file will not work.

Also note that the previous example can be  more  compactly  and  effi-
ciently written (provided the MULTIOS option is set) as:

~~~zsh
paste <(cut -f1 file1) <(cut -f3 file2) \
> >(process1) > >(process2)
~~~

The  shell  uses  pipes  instead  of  FIFOs to implement the latter two
process substitutions in the above example.

There is an additional problem with >(process); when this  is  attached
to  an  external command, the parent shell does not wait for process to
finish and hence an immediately following command cannot  rely  on  the
results  being  complete.   The  problem  and  solution are the same as
described in the section MULTIOS in zshmisc(1).  Hence in a  simplified
version of the example above:

~~~zsh
paste <(cut -f1 file1) <(cut -f3 file2) > >(process)
~~~

(note that no MULTIOS are involved), process will be run asynchronously
as far as the parent shell is concerned.  The workaround is:

~~~zsh
{ paste <(cut -f1 file1) <(cut -f3 file2) } > >(process)
~~~

The extra processes here are spawned from the parent shell  which  will
wait for their completion.

Another problem arises any time a job with a substitution that requires
a temporary file is disowned by the shell,  including  the  case  where
`&!' or `&|' appears at the end of a command containing a substitution.
In that case the temporary file will not be cleaned up as the shell  no
longer  has  any memory of the job.  A workaround is to use a subshell,
for example,

~~~zsh
(mycmd =(myoutput)) &!
~~~

as the forked subshell will wait for the command to finish then  remove
the temporary file.

A  general  workaround  to ensure a process substitution endures for an
appropriate length of time is to pass it as a parameter to an anonymous
shell  function  (a  piece  of  shell code that is run immediately with
function scope). 

For example, this code:

~~~zsh
() {
   print File $1:
   cat $1
} =(print This be the verse)
~~~

outputs something resembling the following

~~~zsh
File /tmp/zsh6nU0kS:
This be the verse
~~~

The temporary file created by the process substitution will be deleted when the function exits.
