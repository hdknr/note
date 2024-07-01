## パスワードハッシュ

~~~php
<?php
require 'wp-includes/class-phpass.php';
$pwd = 'my_cool_password';
$x = new PasswordHash(8, true);
$hash = $x->HashPassword($pwd);
var_dump($hash);
~~
