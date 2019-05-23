# コピーモード

A tmux window may be in one of two modes.  

The default permits direct access to the terminal attached to the window.  

The other is copy mode, which permits a section of a window or its history to be copied to a
paste buffer for later insertion into another window.  

This mode is entered with the copy-mode command, bound to ‘[’ by default.  
It is also entered when a command that produces output, such as list-keys, is executed from a key binding.

Commands are sent to copy mode using the -X flag to the send-keys command.  
When a key is pressed, copy mode automatically uses one of two key tables, depending on the mode-keys option: copy-mode for emacs, 
or copy-mode-vi for vi.  
Key tables may be viewed with the list-keys command.

     The following commands are supported in copy mode:

           Command                              vi              emacs
           append-selection
           append-selection-and-cancel          A
           back-to-indentation                  ^               M-m
           begin-selection                      Space           C-Space
           bottom-line                          L
           cancel                               q               Escape
           clear-selection                      Escape          C-g
           copy-end-of-line                     D               C-k
           copy-line
           copy-pipe <command>
           copy-pipe-and-cancel <command>
           copy-selection
           copy-selection-and-cancel            Enter           M-w
           cursor-down                          j               Down
           cursor-left                          h               Left
           cursor-right                         l               Right
           cursor-up                            k               Up
           end-of-line                          $               C-e
           goto-line <line>                     :               g
           halfpage-down                        C-d             M-Down
           halfpage-down-and-cancel
           halfpage-up                          C-u             M-Up
           history-bottom                       G               M->
           history-top                          g               M-<
           jump-again                           ;               ;
           jump-backward <to>                   F               F
           jump-forward <to>                    f               f
           jump-reverse                         ,               ,
           jump-to-backward <to>                T
           jump-to-forward <to>                 t
           middle-line                          M               M-r
           next-paragraph                       }               M-}
           next-space                           W
           next-space-end                       E
           next-word                            w
           next-word-end                        e               M-f
           other-end                            o
           page-down                            C-f             PageDown
           page-down-and-cancel
           page-up                              C-b             PageUp
           previous-paragraph                   {               M-{
           previous-space                       B
           previous-word                        b               M-b
           rectangle-toggle                     v               R
           scroll-down                          C-e             C-Down
           scroll-down-and-cancel
           scroll-up                            C-y             C-Up
           search-again                         n               n
           search-backward <for>                ?
           search-forward <for>                 /
           search-backward-incremental <for>                    C-r
           search-forward-incremental <for>                     C-s
           search-reverse                       N               N
           select-line                          V
           start-of-line                        0               C-a
           stop-selection
           top-line                             H               M-R

     The ‘-and-cancel’ variants of some commands exit copy mode after they
     have completed (for copy commands) or when the cursor reaches the bot‐
     tom (for scrolling commands).

     The next and previous word keys use space and the ‘-’, ‘_’ and ‘@’
     characters as word delimiters by default, but this can be adjusted by
     setting the word-separators session option.  Next word moves to the
     start of the next word, next word end to the end of the next word and
     previous word to the start of the previous word.  The three next and
     previous space keys work similarly but use a space alone as the word
     separator.

     The jump commands enable quick movement within a line.  For instance,
     typing ‘f’ followed by ‘/’ will move the cursor to the next ‘/’ charac‐
     ter on the current line.  A ‘;’ will then jump to the next occurrence.

     Commands in copy mode may be prefaced by an optional repeat count.
     With vi key bindings, a prefix is entered using the number keys; with
     emacs, the Alt (meta) key and a number begins prefix entry.

     The synopsis for the copy-mode command is:

     copy-mode [-Meu] [-t target-pane]
             Enter copy mode.  The -u option scrolls one page up.  -M begins
             a mouse drag (only valid if bound to a mouse key binding, see
             MOUSE SUPPORT).  -e specifies that scrolling to the bottom of
             the history (to the visible screen) should exit copy mode.
             While in copy mode, pressing a key other than those used for
             scrolling will disable this behaviour.  This is intended to
             allow fast scrolling through a pane's history, for example
             with:

                   bind PageUp copy-mode -eu

## リンク

- [tmux のコピーモードを使ってみる - ようへいの日々精進XP](https://inokara.hateblo.jp/entry/2013/07/04/233051)
