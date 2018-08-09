## メディアの取得

~~~bash
$ curl http://yoursite.com/wordpress/wp-json/wp/v2/posts/88?_embed | jq '._embedded["wp:featuredmedia"][0].media_details.sizes.medium'
~~~

~~~js
{
  "file": "profile-300x200.png",
  "width": 300,
  "height": 200,
  "mime_type": "image/png",
  "source_url": "http://yoursite.com/wordpress/wp-content/uploads/2018/04/profile-300x200.png"
}
~~~

~~~bash
$ curl http://yoursite.com/wordpress/wp-json/wp/v2/posts/88?_embed | jq '._embedded["wp:featuredmedia"][0].media_details.sizes[].source_url'
~~~

~~~js
"http://yoursite.com/wordpress/wp-content/uploads/2018/04/profile-150x150.png"
"http://yoursite.com/wordpress/wp-content/uploads/2018/04/profile-300x200.png"
"http://yoursite.com/wordpress/wp-content/uploads/2018/04/profile-768x512.png"
"http://yoursite.com/wordpress/wp-content/uploads/2018/04/profile-100x100.png"
"http://yoursite.com/wordpress/wp-content/uploads/2018/04/profile.png"
~~~