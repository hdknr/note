rsync: Windows 8.1 にChocolatey でcwrsyncをインストールする

[Chocolatey で cwrsync](http://chocolatey.org/packages/cwrsync)をインストール。
バッチファイルとかが C:\Chocolatey\bin にインストールされます。

    C:\Users\hdknr>cinst cwrsync

    Chocolatey (v0.9.8.23) is installing 'cwrsync' and dependencies. 
    By installing you accept the license for 'cwrsync' 
    and each dependency you are installing.

    ______ cwrsync v5.2.2 ______
    
    Mode                LastWriteTime     Length Name
    ----                -------------     ------ ----
    d----        02/19/2014     15:40            cwrsync

    Downloading cwrsync 64 bit (https://www.itefix.no/i2/sites/all/modules/pubdlcnt/
    pubdlcnt.php?file=https://www.itefix.no/download/cwRsync_5.2.2_Free.zip) 
    to C:\Users\hdknr\AppData\Local\Temp\chocolatey\cwrsync\cwrsyncInstall.zip

    Extracting C:\Users\hdknr\AppData\Local\Temp\chocolatey\cwrsync\cwrsyncInstall.zip 
    to C:\Chocolatey\lib\cwrsync.5.2.2\tools...

    C:\Chocolatey\lib\cwrsync.5.2.2\tools

    cwrsync has finished successfully! The chocolatey gods have answered your request!
    cwrsync has finished successfully! The chocolatey gods have answered your request!

    Adding C:\Chocolatey\bin\rsync.bat and pointing to '%DIR%..\lib\cwrsync.5.2.2\tools\3.1.0\rsync.exe'.
    Adding C:\Chocolatey\bin\rsync and pointing to '%DIR%..\lib\cwrsync.5.2.2\tools\3.1.0\rsync.exe'.
    Adding C:\Chocolatey\bin\ssh-keygen.bat and pointing to '%DIR%..\lib\cwrsync.5.2.2\tools\3.1.0\ssh-keygen.exe'.
    Adding C:\Chocolatey\bin\ssh-keygen and pointing to '%DIR%..\lib\cwrsync.5.2.2\tools\3.1.0\ssh-keygen.exe'.
    Adding C:\Chocolatey\bin\ssh.bat and pointing to '%DIR%..\lib\cwrsync.5.2.2\tools\3.1.0\ssh.exe'.
    Adding C:\Chocolatey\bin\ssh and pointing to '%DIR%..\lib\cwrsync.5.2.2\tools\3.1.0\ssh.exe'.

    Finished installing 'cwrsync' and dependencies - if errors not shown in console,
    none detected. 

    Check log for errors if unsure.


    Reading environment variables from registry. Please wait... Done.


ssh-keygen使える:

    C:\Users\hdknr>ssh-keygen
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/hdknr/.ssh/id_rsa):

GuestのUbuntuにはいってみる:

    C:\Users\hdknr>ssh hdknr@ubuntu.local
    
    Could not create directory '/home/hdknr/.ssh'.
    The authenticity of host 'ubuntu.local (192.168.11.70)' can't be established.
    ECDSA key fingerprint is 63:bc:27:88:d3:96:76:bd:06:59:53:02:3e:81:f3:18.
    Are you sure you want to continue connecting (yes/no)? yes
    Failed to add the host to the list of known hosts (/home/hdknr/.ssh/known_hosts)
    .
    hdknr@ubuntu.local's password:
    Welcome to Ubuntu 13.10 (GNU/Linux 3.11.0-15-generic x86_64)
    
     * Documentation:  https://help.ubuntu.com/
    
     System information disabled due to load higher than 1.0
    
    0 packages can be updated.
    0 updates are security updates.
    
    Last login: Tue Feb 18 09:22:21 2014


rsync.bat:

    C:\Users\hdknr>rsync

    rsync  version 3.1.0  protocol version 31
    Copyright (C) 1996-2013 by Andrew Tridgell, Wayne Davison, and others.
    Web site: http://rsync.samba.org/

    Capabilities:
        64-bit files, 64-bit inums, 32-bit timestamps, 64-bit long ints,
        no socketpairs, hardlinks, symlinks, IPv6, batchfiles, inplace,
        append, ACLs, no xattrs, iconv, symtimes, prealloc
    
    rsync comes with ABSOLUTELY NO WARRANTY.  This is free software, and you
    are welcome to redistribute it under certain conditions.  See the GNU
    General Public Licence for details.
    
    rsync is a file transfer program capable of efficient remote update
    via a fast differencing algorithm.
    
    Usage: rsync [OPTION]... SRC [SRC]... DEST
      or   rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
      or   rsync [OPTION]... SRC [SRC]... [USER@]HOST::DEST
      or   rsync [OPTION]... SRC [SRC]... rsync://[USER@]HOST[:PORT]/DEST
      or   rsync [OPTION]... [USER@]HOST:SRC [DEST]
      or   rsync [OPTION]... [USER@]HOST::SRC [DEST]
      or   rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]
    The ':' usages connect via remote shell, while '::' & 'rsync://' usages connect
    to an rsync daemon, and require SRC or DEST to start with a module name.
    
    Options
     -v, --verbose               increase verbosity
         --info=FLAGS            fine-grained informational verbosity
         --debug=FLAGS           fine-grained debug verbosity
         --msgs2stderr           special output handling for debugging
     -q, --quiet                 suppress non-error messages
         --no-motd               suppress daemon-mode MOTD (see manpage caveat)
     -c, --checksum              skip based on checksum, not mod-time & size
     -a, --archive               archive mode; equals -rlptgoD (no -H,-A,-X)
         --no-OPTION             turn off an implied OPTION (e.g. --no-D)
     -r, --recursive             recurse into directories
     -R, --relative              use relative path names
         --no-implied-dirs       don't send implied dirs with --relative
     -b, --backup                make backups (see --suffix & --backup-dir)
         --backup-dir=DIR        make backups into hierarchy based in DIR
         --suffix=SUFFIX         set backup suffix (default ~ w/o --backup-dir)
     -u, --update                skip files that are newer on the receiver
         --inplace               update destination files in-place (SEE MAN PAGE)
         --append                append data onto shorter files
         --append-verify         like --append, but with old data in file checksum
     -d, --dirs                  transfer directories without recursing
     -l, --links                 copy symlinks as symlinks
     -L, --copy-links            transform symlink into referent file/dir
         --copy-unsafe-links     only "unsafe" symlinks are transformed
         --safe-links            ignore symlinks that point outside the source tree
         --munge-links           munge symlinks to make them safer (but unusable)
     -k, --copy-dirlinks         transform symlink to a dir into referent dir
     -K, --keep-dirlinks         treat symlinked dir on receiver as dir
     -H, --hard-links            preserve hard links
     -p, --perms                 preserve permissions
     -E, --executability         preserve the file's executability
         --chmod=CHMOD           affect file and/or directory permissions
     -A, --acls                  preserve ACLs (implies --perms)
     -o, --owner                 preserve owner (super-user only)
     -g, --group                 preserve group
         --devices               preserve device files (super-user only)
         --specials              preserve special files
     -D                          same as --devices --specials
     -t, --times                 preserve modification times
     -O, --omit-dir-times        omit directories from --times
     -J, --omit-link-times       omit symlinks from --times
         --super                 receiver attempts super-user activities
     -S, --sparse                handle sparse files efficiently
         --preallocate           allocate dest files before writing them
     -n, --dry-run               perform a trial run with no changes made
     -W, --whole-file            copy files whole (without delta-xfer algorithm)
     -x, --one-file-system       don't cross filesystem boundaries
     -B, --block-size=SIZE       force a fixed checksum block-size
     -e, --rsh=COMMAND           specify the remote shell to use
         --rsync-path=PROGRAM    specify the rsync to run on the remote machine
         --existing              skip creating new files on receiver
         --ignore-existing       skip updating files that already exist on receiver
         --remove-source-files   sender removes synchronized files (non-dirs)
         --del                   an alias for --delete-during
         --delete                delete extraneous files from destination dirs
         --delete-before         receiver deletes before transfer, not during
         --delete-during         receiver deletes during the transfer
         --delete-delay          find deletions during, delete after
         --delete-after          receiver deletes after transfer, not during
         --delete-excluded       also delete excluded files from destination dirs
         --ignore-missing-args   ignore missing source args without error
         --delete-missing-args   delete missing source args from destination
         --ignore-errors         delete even if there are I/O errors
         --force                 force deletion of directories even if not empty
         --max-delete=NUM        don't delete more than NUM files
         --max-size=SIZE         don't transfer any file larger than SIZE
         --min-size=SIZE         don't transfer any file smaller than SIZE
         --partial               keep partially transferred files
         --partial-dir=DIR       put a partially transferred file into DIR
         --delay-updates         put all updated files into place at transfer's end
     -m, --prune-empty-dirs      prune empty directory chains from the file-list
         --numeric-ids           don't map uid/gid values by user/group name
         --usermap=STRING        custom username mapping
         --groupmap=STRING       custom groupname mapping
         --chown=USER:GROUP      simple username/groupname mapping
         --timeout=SECONDS       set I/O timeout in seconds
         --contimeout=SECONDS    set daemon connection timeout in seconds
     -I, --ignore-times          don't skip files that match in size and mod-time
     -M, --remote-option=OPTION  send OPTION to the remote side only
         --size-only             skip files that match in size
         --modify-window=NUM     compare mod-times with reduced accuracy
     -T, --temp-dir=DIR          create temporary files in directory DIR
     -y, --fuzzy                 find similar file for basis if no dest file
         --compare-dest=DIR      also compare destination files relative to DIR
         --copy-dest=DIR         ... and include copies of unchanged files
         --link-dest=DIR         hardlink to files in DIR when unchanged
     -z, --compress              compress file data during the transfer
         --compress-level=NUM    explicitly set compression level
         --skip-compress=LIST    skip compressing files with a suffix in LIST
     -C, --cvs-exclude           auto-ignore files the same way CVS does
     -f, --filter=RULE           add a file-filtering RULE
     -F                          same as --filter='dir-merge /.rsync-filter'
                                 repeated: --filter='- .rsync-filter'
         --exclude=PATTERN       exclude files matching PATTERN
         --exclude-from=FILE     read exclude patterns from FILE
         --include=PATTERN       don't exclude files matching PATTERN
         --include-from=FILE     read include patterns from FILE
         --files-from=FILE       read list of source-file names from FILE
     -0, --from0                 all *-from/filter files are delimited by 0s
     -s, --protect-args          no space-splitting; only wildcard special-chars
         --address=ADDRESS       bind address for outgoing socket to daemon
         --port=PORT             specify double-colon alternate port number
         --sockopts=OPTIONS      specify custom TCP options
         --blocking-io           use blocking I/O for the remote shell
         --stats                 give some file-transfer stats
     -8, --8-bit-output          leave high-bit chars unescaped in output
     -h, --human-readable        output numbers in a human-readable format
         --progress              show progress during transfer
     -P                          same as --partial --progress
     -i, --itemize-changes       output a change-summary for all updates
         --out-format=FORMAT     output updates using the specified FORMAT
         --log-file=FILE         log what we're doing to the specified FILE
         --log-file-format=FMT   log updates using the specified FMT
         --password-file=FILE    read daemon-access password from FILE
         --list-only             list the files instead of copying them
         --bwlimit=RATE          limit socket I/O bandwidth
         --outbuf=N|L|B          set output buffering to None, Line, or Block
         --write-batch=FILE      write a batched update to FILE
         --only-write-batch=FILE like --write-batch but w/o updating destination
         --read-batch=FILE       read a batched update from FILE
         --protocol=NUM          force an older protocol version to be used
         --iconv=CONVERT_SPEC    request charset conversion of filenames
         --checksum-seed=NUM     set block/file checksum seed (advanced)
     -4, --ipv4                  prefer IPv4
     -6, --ipv6                  prefer IPv6
         --version               print version number
    (-h) --help                  show this help (-h is --help only if used alone)
    
    Use "rsync --daemon --help" to see the daemon-mode command-line options.

    Please see the rsync(1) and rsyncd.conf(5) man pages for full documentation.

    See http://rsync.samba.org/ for updates, bug reports, and answers
    rsync error: syntax or usage error (code 1) at main.c(1538) [client=3.1.0]
