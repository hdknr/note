# fzf: a command-line fuzzy finder

- fzf is a general-purpose command-line fuzzy finder.

## Homebrew

~~~zsh
$ brew install fzf
==> Downloading https://homebrew.bintray.com/bottles/fzf-0.19.0.catalina.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/0b/0be169ab230f6ff7b2322ee3d61fa0cd44e04300b688d207b67e910d948af442?__gda__=exp=1574393632~hmac=221176534d80234256871704acfee653f5d5d46ee04f7e589aa1b1bc6dae5dfd&response-conten
######################################################################## 100.0%
==> Pouring fzf-0.19.0.catalina.bottle.tar.gz
==> Caveats
To install useful keybindings and fuzzy completion:
  /usr/local/opt/fzf/install

To use fzf in Vim, add the following line to your .vimrc:
  set rtp+=/usr/local/opt/fzf
==> Summary
🍺  /usr/local/Cellar/fzf/0.19.0: 17 files, 3.6MB
~~~

## マニュアル

~~~bash
    fzf [options]
~~~

### OPTIONS

#### Search mode

       -x, --extended

              Extended-search  mode.
              Since 0.10.9, this is enabled by default.
              You can disable it with +x or --no-extended.

       -e, --exact
              Enable exact-match

       -i     Case-insensitive match (default: smart-case match)

       +i     Case-sensitive match

       --literal

              Do not normalize latin script letters for matching.

       --algo=TYPE

              Fuzzy matching algorithm (default: v2)

              v2     Optimal scoring algorithm (quality)
              v1     Faster but not guaranteed  to  find  the  optimal  result
              (performance)


       -n, --nth=N[,..]

              Comma-separated  list  of  field  index expressions for limiting
              search scope.  See FIELD INDEX EXPRESSION for the details.

       --with-nth=N[,..]

              Transform the  presentation  of  each  line  using  field  index
              expressions

       -d, --delimiter=STR

              Field  delimiter  regex  for --nth and --with-nth (default: AWK-
              style)

       --phony

              Do not perform search. With this option, fzf  becomes  a  simple
              selector interface rather than a "fuzzy finder".

#### Search result

       +s, --no-sort

              Do not sort the result

       --tac  Reverse the order of the input

              e.g.
                   history | fzf --tac --no-sort

       --tiebreak=CRI[,..]

              Comma-separated  list  of sort criteria to apply when the scores are tied.

              length  Prefers line with shorter length
              begin   Prefers line with matched substring closer to the beginning
              end     Prefers line with matched substring closer to the end
              index   Prefers line that appeared earlier in the input stream

              - Each criterion should appear only once in the list
              - index is only allowed at the end of the list
              - index is implicitly appended to the list when not specified
              - Default is length (or equivalently length,index)
              - If end is found in the list, fzf will scan each line backwards

#### Interface

       -m, --multi

              Enable multi-select with tab/shift-tab.
              It optionally  takes  an integer  argument which denotes the maximum number of items that can be selected.

       +m, --no-multi

              Disable multi-select

       --no-mouse

              Disable mouse

       --bind=KEYBINDS

              Comma-separated list of custom key bindings. See KEY/EVENT BINDINGS for the details.

       --cycle

              Enable cyclic scroll

       --no-hscroll

              Disable horizontal scroll

       --hscroll-off=COL

              Number of screen columns to keep to the right of the highlighted substring (default: 10).
              Setting it to a large value will  cause the text to be positioned on the center of the screen.

       --filepath-word

              Make  word-wise  movements  and actions respect path separators.
              The following actions are affected:

              backward-kill-word
              backward-word
              forward-word
              kill-word

       --jump-labels=CHARS

              Label characters for jump and jump-accept

#### Layout

       --height=HEIGHT[%]

              Display fzf window  below  the  cursor  with  the  given  height instead of using the full screen.

       --min-height=HEIGHT

              Minimum  height when --height is given in percent (default: 10).
              Ignored when --height is not specified.

       --layout=LAYOUT

              Choose the layout (default: default)

              default       Display from the bottom of the screen
              reverse       Display from the top of the screen
              reverse-list  Display from the top of the screen, prompt at  the
              bottom


       --reverse

              A synonym for --layout=reverse

       --border
       
              Draw border above and below the finder


       --no-unicode
              Use  ASCII  characters instead of Unicode box drawing characters
              to draw border


       --margin=MARGIN

              Comma-separated expression for margins around the finder.

              TRBL     Same margin for top, right, bottom, and left
              TB,RL    Vertical, horizontal margin
              T,RL,B   Top, horizontal, bottom margin
              T,R,B,L  Top, right, bottom, left margin

              Each part can be given in absolute number or in percentage rela-
              tive to the terminal size with % suffix.

              e.g.
                   fzf --margin 10%
                   fzf --margin 1,5%

       --info=STYLE

              Determines the display style of finder info.

              default       Display on the next line to the prompt
              inline        Display on the same line
              hidden        Do not display finder info


       --no-info

              A synonym for --info=hidden


       --prompt=STR

              Input prompt (default: '> ')

       --header=STR

              The given string will be printed as the sticky header. The lines
              are displayed in the given order from top to  bottom  regardless
              of  --layout  option,  and  are not affected by --with-nth. ANSI
              color codes are processed even when --ansi is not set.

       --header-lines=N

              The first N lines of the input are treated as the sticky header.
              When  --with-nth is set, the lines are transformed just like the
              other lines that follow.

#### Display

       --ansi Enable processing of ANSI color codes

       --tabstop=SPACES
              Number of spaces for a tab character (default: 8)

       --color=[BASE_SCHEME][,COLOR:ANSI]
              Color configuration. The name of the base color scheme  is  fol-
              lowed  by  custom  color mappings. Ansi color code of -1 denotes
              terminal default foreground/background color. You can also spec-
              ify 24-bit color in #rrggbb format.

              BASE SCHEME:
                  (default: dark on 256-color terminal, otherwise 16)

                  dark    Color scheme for dark 256-color terminal
                  light   Color scheme for light 256-color terminal
                  16      Color scheme for 16-color terminal
                  bw      No colors

              COLOR:
                  fg      Text
                  bg      Background
                  hl      Highlighted substrings
                  fg+     Text (current line)
                  bg+     Background (current line)
                  gutter  Gutter on the left (defaults to bg+)
                  hl+     Highlighted substrings (current line)
                  info    Info
                  border   Border of the preview window and horizontal separa-
              tors (--border)
                  prompt  Prompt
                  pointer Pointer to the current line
                  marker  Multi-select marker
                  spinner Streaming input indicator
                  header  Header

              EXAMPLES:

                   # Seoul256 theme with 8-bit colors
                   # (https://github.com/junegunn/seoul256.vim)
                   fzf       --color='bg:237,bg+:236,info:143,border:240,spin-
              ner:108' \
                       --color='hl:65,fg:252,header:65,fg+:252' \
                       --color='pointer:161,marker:168,prompt:110,hl+:108'

                   # Seoul256 theme with 24-bit colors
                   fzf       --color='bg:#4B4B4B,bg+:#3F3F3F,info:#BDBB72,bor-
              der:#6B6B6B,spinner:#98BC99' \
                       --color='hl:#719872,fg:#D9D9D9,header:#719872,fg+:#D9D9D9'
              \
                       --color='pointer:#E12672,marker:#E17899,prompt:#98BEDE,hl+:#98BC99'

       --no-bold
              Do not use bold text

       --black
              Use black background

#### History

       --history=HISTORY_FILE
              Load search history from the specified file and update the  file
              on  completion.   When  enabled, CTRL-N and CTRL-P are automati-
              cally remapped to next-history and previous-history.

       --history-size=N
              Maximum number of entries in the history file  (default:  1000).
              The file is automatically truncated when the number of the lines
              exceeds the value.

#### Preview

       --preview=COMMAND
              Execute the given command for the current line and  display  the
              result  on  the  preview window. {} in the command is the place-
              holder that is replaced to the single-quoted string of the  cur-
              rent  line.  To  transform the replacement string, specify field
              index expressions between the braces (See FIELD INDEX EXPRESSION
              for the details).

              e.g.
                   fzf --preview='head -$LINES {}'
                   ls  -l  |  fzf  --preview="echo user={3} when={-4..-2}; cat
              {-1}" --header-lines=1

              fzf exports $FZF_PREVIEW_LINES and $FZF_PREVIEW_COLUMNS so  that
              they  represent  the  exact size of the preview window. (It also
              overrides $LINES and $COLUMNS with the same values but they  can
              be  reset  by  the default shell, so prefer to refer to the ones
              with FZF_PREVIEW_ prefix.)

              A placeholder expression starting with + flag will  be  replaced
              to  the  space-separated list of the selected lines (or the cur-
              rent line if no selection was made) individually quoted.

              e.g.
                   fzf --multi --preview='head -10 {+}'
                   git log --oneline | fzf --multi --preview 'git show {+1}'

              When using a field index expression, leading and trailing white-
              space  is  stripped from the replacement string. To preserve the
              whitespace, use the s flag.

              Also, {q} is replaced to the current query string,  and  {n}  is
              replaced  to  zero-based  ordinal index of the line. Use {+n} if
              you want all index numbers when multiple lines are selected.

              A placeholder expression with f flag is replaced to the path  of
              a  temporary  file that holds the evaluated list. This is useful
              when you multi-select a large number of items and the length  of
              the evaluated string may exceed ARG_MAX.

              e.g.
                   #  Press CTRL-A to select 100K items and see the sum of all
              the numbers.
                   # This won't work properly without 'f' flag due to  ARG_MAX
              limit.
                   seq 100000 | fzf --multi --bind ctrl-a:select-all \
                                    --preview  "awk  '{sum+=} END {print sum}'
              {+f}"

              Note that you can escape a placeholder pattern by  prepending  a
              backslash.

              Preview  window  will be updated even when there is no match for
              the current query if any of the placeholder  expressions  evalu-
              ates to a non-empty string.

       --preview-window=[POSITION][:SIZE[%]][:noborder][:wrap][:hidden]
              Determines  the  layout  of  the preview window. If the argument
              contains :hidden, the preview window will be hidden  by  default
              until  toggle-preview  action is triggered. Long lines are trun-
              cated by default.  Line wrap can be enabled with :wrap flag.

              If size is given as 0, preview window will not be  visible,  but
              fzf will still execute the command in the background.

              POSITION: (default: right)
                  up
                  down
                  left
                  right

              e.g.
                   fzf --preview="head {}" --preview-window=up:30%
                   fzf --preview="file {}" --preview-window=down:1

#### Scripting

       -q, --query=STR
              Start the finder with the given query

       -1, --select-1
              Automatically select the only match

       -0, --exit-0
              Exit immediately when there's no match

       -f, --filter=STR
              Filter  mode.  Do  not  start interactive finder. When used with
              --no-sort, fzf becomes a fuzzy-version of grep.

       --print-query
              Print query as the first line

       --expect=KEY[,..]
              Comma-separated list of keys that can be used to complete fzf in
              addition  to the default enter key. When this option is set, fzf
              will print the name of the key pressed as the first line of  its
              output  (or  as  the second line if --print-query is also used).
              The line will be empty if fzf  is  completed  with  the  default
              enter  key.  If --expect option is specified multiple times, fzf
              will expect the union of the keys. --no-expect  will  clear  the
              list.

              e.g.
                   fzf --expect=ctrl-v,ctrl-t,alt-s --expect=f1,f2,~,@

       --read0
              Read  input delimited by ASCII NUL characters instead of newline
              characters

       --print0
              Print output delimited by ASCII NUL characters instead  of  new-
              line characters

       --no-clear
              Do  not  clear  finder  interface on exit. If fzf was started in
              full screen mode, it  will  not  switch  back  to  the  original
              screen,  so  you'll  have  to manually run tput rmcup to return.
              This option can be used to avoid flickering of the  screen  when
              your application needs to start fzf multiple times in order.

       --sync

              Synchronous search for multi-staged filtering.
              If specified, fzf will launch ncurses finder only after the input stream  is  complete.

              e.g. fzf --multi | fzf --sync

       --version

              Display version information and exit


       Note that most options have the opposite versions with `--no-` prefix. (ネガティブオプション)

### ENVIRONMENT VARIABLES

       FZF_DEFAULT_COMMAND

              Default  command  to use when input is tty.
              On *nix systems, fzf runs the command with sh -c, so make sure that  it's  POSIX-compliant.

       FZF_DEFAULT_OPTS
              Default   options.   e.g.   export  FZF_DEFAULT_OPTS="--extended --cycle"

### EXIT STATUS

       0      Normal exit
       1      No match
       2      Error
       130    Interrupted with CTRL-C or ESC

### FIELD INDEX EXPRESSION

A field index expression can be a non-zero integer or a  range  expression (`[BEGIN]..[END]`).

`--nth` and `--with-nth` take a comma-separated list of field index expressions.

Examples:

       1      The 1st field
       2      The 2nd field
       -1     The last field
       -2     The 2nd to last field
       3..5   From the 3rd field to the 5th field
       2..    From the 2nd field to the last field
       ..-3   From the 1st field to the 3rd to the last field
       ..     All the fields

### EXTENDED SEARCH MODE

Unless specified otherwise, fzf will start in  "extended-search  mode".
In  this  mode,  you can specify multiple patterns delimited by spaces, such as: 'wild ^music .mp3$ sbtrkt !rmx

You can prepend a backslash to a space (\ ) to match  a  literal  space character.

#### Exact-match (quoted)

A  term that is prefixed by a single-quote character (') is interpreted as an "exact-match" (or "non-fuzzy") term.  fzf  will  search  for  the exact occurrences of the string.

#### Anchored-match

A  term  can  be prefixed by ^, or suffixed by $ to become an anchored-
match term. Then fzf will search for the lines that start with  or  end
with  the  given  string. An anchored-match term is also an exact-match term.

#### Negation

If a term is prefixed by !, fzf will exclude the lines that satisfy the term  from  the  result.  In  this  case,  fzf  performs exact match by default.

#### Exact-match by default

If you don't prefer fuzzy matching and do not wish to "quote"  (prefix- ing  with ') every word, start fzf with -e or --exact option. 
Note that when --exact is set, '-prefix "unquotes" the term.


#### OR operator

A single bar character term acts as an OR operator.  For  example,  the
following  query  matches  entries  that  start  with core and end with
either go, rb, or py.

e.g. ^core go$ | rb$ | py$

### KEY/EVENT BINDINGS

       --bind option allows you to bind a key or  an  event  to  one  or  more
       actions.  You can use it to customize key bindings or implement dynamic
       behaviors.

       --bind takes a comma-separated list of binding expressions. Each  bind-
       ing expression is KEY:ACTION or EVENT:ACTION.

       e.g.
            fzf --bind=ctrl-j:accept,ctrl-k:kill-line


   AVAILABLE KEYS: (SYNONYMS)

       ctrl-[a-z]
       ctrl-space
       ctrl-\
       ctrl-]
       ctrl-^      (ctrl-6)
       ctrl-/      (ctrl-_)
       ctrl-alt-[a-z]
       alt-[a-z]
       alt-[0-9]
       f[1-12]
       enter       (return ctrl-m)
       space
       bspace      (bs)
       alt-up
       alt-down
       alt-left
       alt-right
       alt-enter
       alt-space
       alt-bspace  (alt-bs)
       alt-/
       tab
       btab        (shift-tab)
       esc
       del
       up
       down
       left
       right
       home
       end
       pgup        (page-up)
       pgdn        (page-down)
       shift-up
       shift-down
       shift-left
       shift-right
       left-click
       right-click
       double-click
       or any single character


   AVAILABLE EVENTS:
       change (triggered whenever the query string is changed)

           e.g.
                #  Moves  cursor  to the top (or bottom depending on --layout)
       whenever the query is changed
                fzf --bind change:top


   AVAILABLE ACTIONS:
       A key or an event can be bound to one or more of the following actions.

         ACTION:               DEFAULT BINDINGS (NOTES):
           abort                 ctrl-c  ctrl-g  ctrl-q  esc
           accept                enter   double-click
           accept-non-empty       (same  as accept except that it prevents fzf
       from exiting without selection)
           backward-char         ctrl-b  left
           backward-delete-char  ctrl-h  bspace
           backward-kill-word    alt-bs
           backward-word         alt-b   shift-left
           beginning-of-line     ctrl-a  home
           cancel                (clears query string if not empty, aborts fzf
       otherwise)
           clear-screen          ctrl-l
           delete-char           del
           delete-char/eof       ctrl-d
           deselect-all
           down                  ctrl-j  ctrl-n  down
           end-of-line           ctrl-e  end
           execute(...)          (see below for the details)
           execute-silent(...)   (see below for the details)
           execute-multi(...)    (deprecated in favor of {+} expression)
           forward-char          ctrl-f  right
           forward-word          alt-f   shift-right
           ignore
           jump                  (EasyMotion-like 2-keystroke movement)
           jump-accept           (jump and accept)
           kill-line
           kill-word             alt-d
           next-history          (ctrl-n on --history)
           page-down             pgdn
           page-up               pgup
           half-page-down
           half-page-up
           preview-down          shift-down
           preview-up            shift-up
           preview-page-down
           preview-page-up
           previous-history      (ctrl-p on --history)
           print-query           (print query and exit)
           reload(...)           (see below for the details)
           replace-query         (replace query string with the current selec-
       tion)
           select-all
           toggle                (right-click)
           toggle-all
           toggle+down           ctrl-i  (tab)
           toggle-in             (--layout=reverse* ? toggle+up : toggle+down)
           toggle-out            (--layout=reverse* ? toggle+down : toggle+up)
           toggle-preview
           toggle-preview-wrap
           toggle-sort
           toggle+up             btab    (shift-tab)
           top                   (move to the top result)
           unix-line-discard     ctrl-u
           unix-word-rubout      ctrl-w
           up                    ctrl-k  ctrl-p  up
           yank                  ctrl-y


   ACTION COMPOSITION

       Multiple actions can be chained using + separator.

       e.g.
            fzf --bind 'ctrl-a:select-all+accept'


   COMMAND EXECUTION

       With execute(...) action, you can execute  arbitrary  commands  without
       leaving  fzf.  For example, you can turn fzf into a simple file browser
       by binding enter key to less command like follows.

           fzf --bind "enter:execute(less {})"

       You can use the same placeholder expressions as in --preview.

       If the command contains parentheses, fzf may fail to parse the  expres-
       sion.  In that case, you can use any of the following alternative nota-
       tions to avoid parse errors.

           execute[...]
           execute~...~
           execute!...!
           execute@...@
           execute#...#
           execute$...$
           execute%...%
           execute^...^
           execute&...&
           execute*...*
           execute;...;
           execute/.../
           execute|...|
           execute:...
              The last one is the special  form  that  frees  you  from  parse
              errors as it does not expect the closing character. The catch is
              that it should be the last one in the  comma-separated  list  of
              key-action pairs.

       fzf switches to the alternate screen when executing a command. However,
       if the command is expected to complete quickly, and you are not  inter-
       ested  in  its  output,  you  might want to use execute-silent instead,
       which silently executes the command without the  switching.  Note  that
       fzf will not be responsive until the command is complete. For asynchro-
       nous execution, start  your  command  as  a  background  process  (i.e.
       appending &).


   RELOAD INPUT

       reload(...) action is used to dynamically update the input list without
       restarting fzf. It takes the same  command  template  with  placeholder
       expressions as execute(...).

       See https://github.com/junegunn/fzf/issues/1750 for more info.

       e.g.
            # Update the list of processes by pressing CTRL-R
            ps -ef | fzf --bind 'ctrl-r:reload(ps -ef)' --header 'Press CTRL-R
       to reload' \
                         --header-lines=1 --layout=reverse

            # Integration with ripgrep
            RG_PREFIX="rg --column --line-number  --no-heading  --color=always
       --smart-case "
            INITIAL_QUERY="foobar"
            FZF_DEFAULT_COMMAND="$RG_PREFIX '$INITIAL_QUERY'" \
              fzf --bind "change:reload:$RG_PREFIX {q} || true" \
                  --ansi --phony --query "$INITIAL_QUERY"

### SEE ALSO

- Project homepage: https://github.com/junegunn/fzf
- Extra Vim plugin: https://github.com/junegunn/fzf.vim
