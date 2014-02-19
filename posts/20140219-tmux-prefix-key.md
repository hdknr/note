Date: 2014-02-19  13:30
Title:  tmux:ネスト先のプレフィックスキーを変更
Type: post  
Excerpt:   


tmux起動のローカルサーバーからsshでログイン先でtmux使う場合、同じプレフィックスの場合があるのでコマンドで変更する。

BキーからTキーに変更:

    $ tmux unbind-key C-b
    $ tmux set-option -g prefix C-t
    $ tmux bind-key C-t send-prefix
    
今のプレフィックキーを確認:

    $ tmux list-keys |  grep prefix

    bind-key          a send-prefix    