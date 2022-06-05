# fc  (history)

       fc [ -e ename ] [ -LI ] [ -m match ] [ old=new ... ] [ first [ last ] ]
       fc -l [ -LI ] [ -nrdfEiD ] [ -t timefmt ] [ -m match ]
             [ old=new ... ] [ first [ last ] ]
       fc -p [ -a ] [ filename [ histsize [ savehistsize ] ] ]
       fc -P
       fc -ARWI [ filename ]

## 内容

The fc command controls the interactive history mechanism.  
Note that reading and writing of history options is only performed if the shell is interactive.  
Usually this is detected automatically,
but it can be forced by setting the interactive option when starting the shell.

### 範囲

From / To:

The first two forms of this command select a range of events from `first` to `last` from the history list.  
The arguments `first` and `last` may be specified as a number or as a string.  

オフセット:

A negative number is used as an offset to the current history event number.  
A string specifies the most recent event beginning with the given string.  
All substitutions old=new, if any, are then performed on the text of the events.

In addition to the number range,

    -I     restricts to only internal events (not from `$HISTFILE`)

    -L     restricts to only local events 
           (not from other shells, see SHARE_HISTORY in [zshoptions(1)](zshoptions.md) 
           -- note that `$HISTFILE` is considered local when read at startup)

    -m     takes the first argument as a pattern (should be quoted) 
           and only the history events matching this pattern are considered

`-l`:

If first is not specified, it will be set to -1 (the most recent event), or to -16 if the -l flag is given.  
If last is not specified, it will be set to first, or to -1 if the -l flag is given.

However, if the current event has added entries to the history with `print -s` or `fc -R`, 
then the default last for -l includes all new history entries since the current event began.

When the -l flag is given, the resulting events are listed on standard output.  
Otherwise the editor program specified by `-e ename` is invoked on a file containing these history events.  

`-e`:

If -e is not given, the value of the parameter FCEDIT is used; 
if that is not set the value of the parameter EDITOR is used; 
if that is not set a builtin default, usually `vi` is used.  If `ename` is `-`, no editor is invoked.  
When editing is complete, the edited command is executed.

`-r`(逆) `-n`(番号なし) :

The flag -r reverses the order of the events and the flag -n suppresses event numbers when listing.

Also when listing,

    -d     prints timestamps for each event
    -f     prints full time-date stamps in the US `MM/DD/YY hh:mm' format
    -E     prints full time-date stamps in the European `dd.mm.yyyy hh:mm' format
    -i     prints full time-date stamps in ISO8601 `yyyy-mm-dd hh:mm' format
    -t fmt prints time and date stamps in the given format; fmt is formatted with the strftime function with the zsh extensions described for the %D{string} prompt format in the section EXPANSION OF
           PROMPT SEQUENCES in zshmisc(1).  The resulting formatted string must be no more than 256 characters or will not be printed
    -D     prints elapsed times; may be combined with one of the options above

`fc -p` pushes the current history list onto a stack and switches to a new history list.  
If the -a option is also specified, 
this history list will be automatically popped when the current function scope is exited, 
which is a much better solution than creating a trap function to call `fc -P` manually.  

If no arguments are specified, 
the history list is left empty, `$HISTFILE` is unset, 
and `$HISTSIZE` & `$SAVEHIST` are set to their default values.  
If one argument is given, `$HISTFILE` is set to that filename, 
$HISTSIZE & $SAVEHIST are left unchanged, 
and the history file is read in (if it exists) to initialize the new list.  

If a second argument is specified, 
`$HISTSIZE` & `$SAVEHIST` are instead set to the single specified numeric value.  

Finally, if a third argument is specified, 
`$SAVEHIST` is set to a separate value from `$HISTSIZE`.  
You are free to change these environment values for the new history list however you desire in order to manipulate the new history list.

`fc -P` pops the history list back to an older list saved by `fc -p`.  
The current list is saved to its `$HISTFILE` before it is destroyed 
(assuming that `$HISTFILE` and `$SAVEHIST` are set appropriately, of course).  

The values of `$HISTFILE`, `$HISTSIZE`, and `$SAVEHIST` are restored to the values they had 
when `fc -p` was called.  

Note that this restoration can conflict with making these variables "local", 
so your best bet is to avoid local declarations for these variables in functions that use `fc -p`  

The one other guaranteed-safe combination is declaring these variables to be local 
at the top of your function and using the automatic option (-a) with `fc -p`.  

Finally, 
note that it is legal to manually pop a push marked for automatic popping 
if you need to do so before the function exits.

`fc -R` reads the history from the given file, 
`fc -W` writes the history out to the given file, 
and `fc -A` appends the history out to the given file.  

If no filename is specified, the `$HISTFILE` is assumed.  
If the -I option is added to -R, 
only those events that are not already contained within the internal history list are added.  
If the -I option is added to -A or -W, 
only those events that are new since last incremental append/write to the history file are appended/written.  

In any case, the created file will have no more than `$SAVEHIST` entries.

## 変数

| 変数名   | 意味                                                       |
| -------- | ---------------------------------------------------------- |
| HISTSIZE | メモリに保存される履歴の件数。(保存数だけ履歴を検索できる) |
| SAVEHIST | HISTFILE で指定したファイルに保存される履歴の件数          |
| HISTFILE | 履歴ファイルの保存先                                       |

例:

~~~zsh
export HISTFILE=${HOME}/.zsh_history
export HISTSIZE=1000
export SAVEHIST=100000
~~~

### 例

全ての履歴:

~~~zsh
% history 1
~~~

## 資料

- `man zshbuiltins`
- [mac の zsh で history するときのメモ](https://qiita.com/YKInoMT/items/2cbd0f7714197591e02e)
