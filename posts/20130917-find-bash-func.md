Date: 2013-09-17  05:00
Title:  bash:find で関数を呼ぶ
Type: post  
Excerpt:   

直接出来ないので、-exec でbashを呼ぶとよい:


    !/bin/bash
    
    DIST=/usr/share/scala

    makelink()
    {
     echo "sudo ln -s $1 /usr/bin/`basename $1`"
     sudo ln -s $1 /usr/bin/`basename $1`
    }

    export -f makelink
    
    find $DIST/bin/* -maxdepth 0  -not -name "*.bat"  -exec bash -c 'makelink {}' \;

ちなみに Debian Wheezyのscalaは 2.9.2 っぽいからそれを使うかな。
