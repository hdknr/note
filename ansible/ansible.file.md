- [[Ansible] ディレクトリが無かったら作成する](http://qiita.com/hnakamur/items/b5a17d8cb289432014d5)

~~~yaml
- name: nginx location config file directory
  file: path=/etc/nginx/conf.d/location.d state=directory owner=root group=root mode=0755
~~~  
