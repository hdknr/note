Date: 2014-01-16  13:00
Title: Homebrew: update でエラー ( git reset --hard orgin/master)
Type: post  
Excerpt:   



[写経](http://blog.f13.jp/post/20626146392/brew-brew-update) :

更新失敗:

    PeekoOne:local hide$ brew update
    
    Error: Failure while executing: git pull -q origin refs/heads/master:refs/remotes/origin/master
    
    
移動:

    PeekoOne:~ hide$ cd `brew --prefix`
    
    PeekoOne:local hide$ pwd
    /usr/local

originを取って来る:
    
    PeekoOne:local hide$ git fetch origin
    remote: Counting objects: 242, done.
    remote: Compressing objects: 100% (107/107), done.
    remote: Total 230 (delta 95), reused 223 (delta 88)
    Receiving objects: 100% (230/230), 51.95 KiB, done.
    Resolving deltas: 100% (95/95), completed with 3 local objects.
    From https://github.com/mxcl/homebrew
       8a968e9..6305d2d  gh-pages   -> origin/gh-pages
     * [new branch]      go         -> origin/go
     
ハードリセットします([git-reset](https://www.kernel.org/pub/software/scm/git/docs/git-reset.html)):

    PeekoOne:local hide$ git reset --hard origin/master
    Checking out files: 100% (1497/1497), done.
    HEAD is now at 6aa59e5 openssl: use https for download
    
再度更新：    
    
    PeekoOne:local hide$ cd
    PeekoOne:~ hide$ brew update
    Already up-to-date.


エラーはでなくなった。
