## REPL

~~~
$ xcrun swift
~~~

~~~
Welcome to Swift version 1.2. Type :help for assistance.
  1>  
~~~

~~~
The Swift REPL (Read-Eval-Print-Loop) acts like an interpreter.  Valid statements, expressions, and declarations are immediately
compiled and executed.

The complete set of LLDB debugging commands are also available as described below.  Commands must be prefixed with a colon at the REPL
prompt (:quit for example.)  Typing just a colon followed by return will switch to the LLDB prompt.

Debugger commands:

  apropos           -- Find a list of debugger commands related to a particular word/subject.
  breakpoint        -- A set of commands for operating on breakpoints. Also see _regexp-break.
  command           -- A set of commands for managing or customizing the debugger commands.
  disassemble       -- Disassemble bytes in the current function, or elsewhere in the executable program as specified by the user.
  expression        -- Evaluate an expression (ObjC++ or Swift) in the current program context, using user defined variables and
                       variables currently in scope.
  frame             -- A set of commands for operating on the current thread's frames.
  gdb-remote        -- Connect to a remote GDB server.  If no hostname is provided, localhost is assumed.
  gui               -- Switch into the curses based GUI mode.
  help              -- Show a list of all debugger commands, or give details about specific commands.
  kdp-remote        -- Connect to a remote KDP server.  udp port 41139 is the default port number.
  log               -- A set of commands for operating on logs.
  memory            -- A set of commands for operating on memory.
  platform          -- A set of commands to manage and create platforms.
  plugin            -- A set of commands for managing or customizing plugin commands.
  process           -- A set of commands for operating on a process.
  quit              -- Quit out of the LLDB debugger.
  register          -- A set of commands to access thread registers.
  script            -- Pass an expression to the script interpreter for evaluation and return the results. Drop into the interactive
                       interpreter if no expression is given.
  settings          -- A set of commands for manipulating internal settable debugger variables.
  source            -- A set of commands for accessing source file information
  target            -- A set of commands for operating on debugger targets.
  thread            -- A set of commands for operating on one or more threads within a running process.
  type              -- A set of commands for operating on the type system
  version           -- Show version of LLDB debugger.
  watchpoint        -- A set of commands for operating on watchpoints.

Current command abbreviations (type ':help command alias' for more info):

  add-dsym  -- ('target symbols add')  Add a debug symbol file to one of the target's current modules by specifying a path to a debug
               symbols file, or using the options to specify a module to download symbols for.
  attach    -- ('_regexp-attach')  Attach to a process id if in decimal, otherwise treat the argument as a process name to attach to.
  b         -- ('_regexp-break')  Set a breakpoint using a regular expression to specify the location, where <linenum> is in decimal
               and <address> is in hex.
  bt        -- ('_regexp-bt')  Show a backtrace.  An optional argument is accepted; if that argument is a number, it specifies the
               number of frames to display.  If that argument is 'all', full backtraces of all threads are displayed.
  c         -- ('process continue')  Continue execution of all threads in the current process.
  call      -- ('expression --')  Evaluate an expression (ObjC++ or Swift) in the current program context, using user defined variables
               and variables currently in scope.
  continue  -- ('process continue')  Continue execution of all threads in the current process.
  detach    -- ('process detach')  Detach from the current process being debugged.
  di        -- ('disassemble')  Disassemble bytes in the current function, or elsewhere in the executable program as specified by the
               user.
  dis       -- ('disassemble')  Disassemble bytes in the current function, or elsewhere in the executable program as specified by the
               user.
  display   -- ('_regexp-display')  Add an expression evaluation stop-hook.
  down      -- ('_regexp-down')  Go down "n" frames in the stack (1 frame by default).
  env       -- ('_regexp-env')  Implements a shortcut to viewing and setting environment variables.
  exit      -- ('quit')  Quit out of the LLDB debugger.
  f         -- ('frame select')  Select a frame by index from within the current thread and make it the current frame.
  file      -- ('target create')  Create a target using the argument as the main executable.
  finish    -- ('thread step-out')  Finish executing the function of the currently selected frame and return to its call site in
               specified thread (current thread, if none specified).
  image     -- ('target modules')  A set of commands for accessing information for one or more target modules.
  j         -- ('_regexp-jump')  Sets the program counter to a new address.
  jump      -- ('_regexp-jump')  Sets the program counter to a new address.
  kill      -- ('process kill')  Terminate the current process being debugged.
  l         -- ('_regexp-list')  Implements the GDB 'list' command in all of its forms except FILE:FUNCTION and maps them to the
               appropriate 'source list' commands.
  list      -- ('_regexp-list')  Implements the GDB 'list' command in all of its forms except FILE:FUNCTION and maps them to the
               appropriate 'source list' commands.
  n         -- ('thread step-over')  Source level single step in specified thread (current thread, if none specified), stepping over
               calls.
  next      -- ('thread step-over')  Source level single step in specified thread (current thread, if none specified), stepping over
               calls.
  nexti     -- ('thread step-inst-over')  Single step one instruction in specified thread (current thread, if none specified), stepping
               over calls.
  ni        -- ('thread step-inst-over')  Single step one instruction in specified thread (current thread, if none specified), stepping
               over calls.
  p         -- ('expression --')  Evaluate an expression (ObjC++ or Swift) in the current program context, using user defined variables
               and variables currently in scope.
  po        -- ('expression -O  -- ')  Evaluate an expression (ObjC++ or Swift) in the current program context, using user defined
               variables and variables currently in scope.
  print     -- ('expression --')  Evaluate an expression (ObjC++ or Swift) in the current program context, using user defined variables
               and variables currently in scope.
  q         -- ('quit')  Quit out of the LLDB debugger.
  r         -- ('process launch -c /bin/sh --')  Launch the executable in the debugger.
  rbreak    -- ('breakpoint set -r %1')  Sets a breakpoint or set of breakpoints in the executable.
  repl      -- ('expression -r  -- ')  Evaluate an expression (ObjC++ or Swift) in the current program context, using user defined
               variables and variables currently in scope.
  run       -- ('process launch -c /bin/sh --')  Launch the executable in the debugger.
  s         -- ('thread step-in')  Source level single step in specified thread (current thread, if none specified).
  si        -- ('thread step-inst')  Single step one instruction in specified thread (current thread, if none specified).
  step      -- ('thread step-in')  Source level single step in specified thread (current thread, if none specified).
  stepi     -- ('thread step-inst')  Single step one instruction in specified thread (current thread, if none specified).
  t         -- ('thread select')  Select a thread as the currently active thread.
  tbreak    -- ('_regexp-tbreak')  Set a one shot breakpoint using a regular expression to specify the location, where <linenum> is in
               decimal and <address> is in hex.
  undisplay -- ('_regexp-undisplay')  Remove an expression evaluation stop-hook.
  up        -- ('_regexp-up')  Go up "n" frames in the stack (1 frame by default).
  x         -- ('memory read')  Read from the memory of the process being debugged.
~~~

### ライブラリのロード

~~~
$ xcrun swift -I "./" -L "./" -lYourClass -sdk $(xcrun --show-sdk-path --sdk macosx) 
~~~

### import

~~~
  3> var ierror: NSError?
repl.swift:3:13: error: use of undeclared type 'NSError'
var ierror: NSError?
            ^~~~~~~
~~~

~~~
  3> import Foundation
~~~

~~~
  4> var ierror: NSError?
ierror: NSError? = nil
~~~