# wp-json

## ルートの一覧

~~~bash 
$ curl  -s http://192.168.56.54:8080/wp-json/ | jq ".routes | keys"
[
  "/",
  "/oembed/1.0",
  "/oembed/1.0/embed",
  "/oembed/1.0/proxy",
  "/wp/v2",
  "/wp/v2/categories",
  "/wp/v2/categories/(?P<id>[\\d]+)",
  "/wp/v2/comments",
  "/wp/v2/comments/(?P<id>[\\d]+)",
  "/wp/v2/media",
  "/wp/v2/media/(?P<id>[\\d]+)",
  "/wp/v2/pages",
  "/wp/v2/pages/(?P<id>[\\d]+)",
  "/wp/v2/pages/(?P<parent>[\\d]+)/revisions",
  "/wp/v2/pages/(?P<parent>[\\d]+)/revisions/(?P<id>[\\d]+)",
  "/wp/v2/posts",
  "/wp/v2/posts/(?P<id>[\\d]+)",
  "/wp/v2/posts/(?P<parent>[\\d]+)/revisions",
  "/wp/v2/posts/(?P<parent>[\\d]+)/revisions/(?P<id>[\\d]+)",
  "/wp/v2/settings",
  "/wp/v2/statuses",
  "/wp/v2/statuses/(?P<status>[\\w-]+)",
  "/wp/v2/tags",
  "/wp/v2/tags/(?P<id>[\\d]+)",
  "/wp/v2/taxonomies",
  "/wp/v2/taxonomies/(?P<taxonomy>[\\w-]+)",
  "/wp/v2/types",
  "/wp/v2/types/(?P<type>[\\w-]+)",
  "/wp/v2/users",
  "/wp/v2/users/(?P<id>[\\d]+)",
  "/wp/v2/users/me"
]
~~~

## 記事 "/wp/v2/posts"

一覧

~~~bash
$ curl  -s http://192.168.56.54:8080/wp-json/wp/v2/posts | jq ".[].title.rendered"
"Hello world!"
"Ratione distinctio repellendus ut id ut."
"Enim neque voluptas qui qui."
"Non ipsum illo voluptas cupiditate amet nihil eum."
"Aspernatur nostrum illum vero."
"Ipsam consequatur incidunt quia in asperiores."
"Aut aut nihil impedit eum ea quae et."
"Est fuga est excepturi excepturi est."
"Aliquam repellat tempora modi aut molestiae est quisquam."
"Quis est facilis sit magni."
~~~

Pythonでクロール:

~~~py
import click 
import requests

@click.group()
def main():
    pass


@main.command()
@click.argument('site')
def crawl(site):
    url = f"{site}/wp-json/wp/v2/posts"
    count = 0

    res = requests.get(url)
    while res and res.status_code == 200:
        with open(f"{count}.json", "w") as out:
            out.write(res.content.decode('utf8'))

        next_link = res.links['next'] and res.links['next']['url']
        if next_link:
            count = count + 1
            res = requests.get(next_link)
        else:
            break

if __name__ == '__main__':
    main()
~~~

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