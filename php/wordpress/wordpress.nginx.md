## /home で nginx からwordpresを動かす


~~~
location /home {

  alias /home/ubuntu/projects/wordpress;
  try_files $uri $uri/ /home/index.php?args;
  index index.php;

  location ~ \.php$ {
    fastcgi_split_path_info ^(.+\.php)(/.*)$;
    fastcgi_pass phpfpm;
    fastcgi_index index.php;
    fastcgi_param SCRIPT_FILENAME $request_filename;
    fastcgi_param PATH_INFO $fastcgi_script_name;
    fastcgi_param HTTP_PROXY "";
    include fastcgi_params;
  }
}
~~~
