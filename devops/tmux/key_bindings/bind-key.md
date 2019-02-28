# bind-key (alias: bind)

~~~bash
bind-key [-nr] [-T key-table] key command [arguments]
~~~

Bind key key to command.  

To view the default bindings and possible commands, see the list-keys command.

Keys are bound in a key table.  

By default (without -T), the key is bound in the prefix key table.  

This table is used for keys pressed after the prefix key
(for example, by default ‘c’ is bound to new-window in the prefix table, 
so ‘C-b c’ creates a new window).  

The root table is used for keys pressed without the prefix key: 
binding ‘c’ to new-window in the root table (not recommended) means a plain ‘c’ will create a new window.  

## `-n`

-n is an alias for -T root.  

## `-T`

Keys may also be bound in custom key tables 
and the switch-client -T command used to switch to them from a key binding.  

## `-r`

The -r flag indicates this key may repeat, see the repeat-time option.
