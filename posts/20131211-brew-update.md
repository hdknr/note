Date: 2013-12-11 3:00 
Title: Homebrew: Error: undefined method `to_sym' for nil:NilClass  
Type: post  
Excerpt:   




update でエラー:

    (docs)Peeko:identity hide$ brew update

    Error: undefined method `to_sym' for nil:NilClass
    Please report this bug:
        https://github.com/mxcl/homebrew/wiki/troubleshooting
    /usr/local/Library/Homebrew/cmd/update.rb:134:in `report'
    /usr/local/Library/Homebrew/cmd/update.rb:132:in `each_line'
    /usr/local/Library/Homebrew/cmd/update.rb:132:in `report'
    /usr/local/Library/Homebrew/cmd/update.rb:36:in `update'
    /usr/local/Library/brew.rb:95:in `send'
    /usr/local/Library/brew.rb:95


[Issues#24286](https://github.com/mxcl/homebrew/issues/24286) にある。


もう一回やると OK:

    (docs)Peeko:identity hide$ brew update
    Already up-to-date.


doctorすると問題あったので更新:

    (docs)Peeko:identity hide$ brew doctor
    Warning: Your XQuartz (2.7.4) is outdated
    Please install XQuartz 2.7.5:
      https://xquartz.macosforge.org
    
    Warning: Homebrew's sbin was not found in your PATH but you have installed
    formulae that put executables in /usr/local/sbin.
    Consider setting the PATH for example like so
        echo export PATH="/usr/local/sbin:$PATH" >> ~/.bash_profile
    
    

    
