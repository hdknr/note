# wget

##  `-m` /  `--mirror`

Turn on options suitable for mirroring. 
This option turns on recursion and time-stamping, sets infinite recursion depth and keeps FTP directory listings. 
It is currently equivalent to `-r -N -l inf --no-remove-listing`.


## `-K` / `--backup-converted`

When converting a file, back up the original version with a .orig suffix. 
Affects the behavior of `-N`.


## `-k` / `--convert-links`

After the download is complete, convert the links in the document to make them suitable for local viewing. 
This affects not only the visible hyperlinks, but any part of the document that links to external content, 
such as embedded images, links to style sheets, hyperlinks to non-HTML content, etc.
Each link will be changed in one of the two ways:

â€¢ The links to files that have been downloaded by Wget will be changed to refer to the file they point to as a relative link.
Example: if the downloaded file /foo/doc.html links to /bar/img.gif, also downloaded, then the link in doc.html will be modified to point to ../bar/img.gif. This kind of transformation works reliably for arbitrary combinations of directories.
â€¢ The links to files that have not been downloaded by Wget will be changed to include host name and absolute path of the location they point to.
Example: if the downloaded file /foo/doc.html links to /bar/img.gif (or to ../bar/img.gif), then the link in doc.html will be modified to point to http://hostname/bar/img.gif.

Because of this, local browsing works reliably: if a linked file was downloaded, the link will refer to its local name; if it was not downloaded, the link will refer to its full Internet address rather than presenting a broken link. The fact that the former links are converted to relative links ensures that you can move the downloaded hierarchy to another directory.
Note that only at the end of the download can Wget know which links have been downloaded. Because of that, the work done by -k will be performed at the end of all the downloads.

## `-E` /  `--adjust-extension`

If a file of type application/xhtml+xml or text/html is downloaded and the URL does not end with the regexp \.[Hh][Tt][Mm][Ll]?, this option will cause the suffix .html to be appended to the local filename. This is useful, for instance, when you're mirroring a remote site that uses .asp pages, but you want the mirrored pages to be viewable on your stock Apache server. Another good use for this is when you're downloading CGI-generated materials. A URL like http://site.com/article.cgi?25 will be saved as article.cgi?25.html.
Note that filenames changed in this way will be re-downloaded every time you re-mirror a site, because Wget can't tell that the local X.html file corresponds to remote URL X (since it doesn't yet know that the URL produces output of type text/html or application/xhtml+xml. To prevent this re-downloading, you must use -k and -K so that the original version of the file will be saved as X.orig.

As of version 1.12, Wget will also ensure that any downloaded files of type text/css end in the suffix .css, and the option was renamed from --html-extension, to better reflect its new behavior. The old option name is still acceptable, but should now be considered deprecated.

At some point in the future, this option may well be expanded to include suffixes for other types of content, including content types that are not parsed by Wget.


## `-l depth` / `--level=depth`

Specify recursion maximum depth level depth. The default maximum depth is 5.

## `-t number` / `--tries=number`

Set number of retries to number. 
Specify 0 or inf for infinite retrying. 
The default is to retry 20 times, with the exception of fatal errors like "connection refused" or "not found" (404), which are not retried.




## `-p` /  `--page-requisites`

This option causes Wget to download all the files that are necessary to properly display a given HTML page. This includes such things as inlined images, sounds, and referenced stylesheets.
Ordinarily, when downloading a single HTML page, any requisite documents that may be needed to display it properly are not downloaded. Using -r together with -l can help, but since Wget does not ordinarily distinguish between external and inlined documents, one is generally left with "leaf documents" that are missing their requisites.

For instance, say document 1.html contains an "`<IMG>`" tag referencing 1.gif and an "``<A>``" tag pointing to external document 2.html. Say that 2.html is similar but that its image is 2.gif and it links to 3.html. Say this continues up to some arbitrarily high number.

If one executes the command:

wget -r -l 2 http://`<site>`/1.html
then 1.html, 1.gif, 2.html, 2.gif, and 3.html will be downloaded. As you can see, 3.html is without its requisite 3.gif because Wget is simply counting the number of hops (up to 2) away from 1.html in order to determine where to stop the recursion. However, with this command:
wget -r -l 2 -p http://`<site>`/1.html
all the above files and 3.html's requisite 3.gif will be downloaded. Similarly,
wget -r -l 1 -p http://`<site>`/1.html
will cause 1.html, 1.gif, 2.html, and 2.gif to be downloaded. One might think that:
wget -r -l 0 -p http://`<site>`/1.html
would download just 1.html and 1.gif, but unfortunately this is not the case, because -l 0 is equivalent to -l inf---that is, infinite recursion. To download a single HTML page (or a handful of them, all specified on the command-line or in a -i URL input file) and its (or their) requisites, simply leave off -r and -l:
wget -p http://`<site>`/1.htm:
Note that Wget will behave as if -r had been specified, but only that single page and its requisites will be downloaded. Links from that page to external documents will not be followed. Actually, to download a single page and all its requisites (even if they exist on separate websites), and make sure the lot displays properly locally, this author likes to use a few options in addition to -p:
wget -E -H -k -K -p http://`<site>`/`<document>`
To finish off this topic, it's worth knowing that Wget's idea of an external document link is any URL specified in an "`<A>`" tag, an "`<AREA>`" tag, or a "`<LINK>`" tag other than "`<LINK REL="stylesheet">`".

## オプション

| 引数（略式表記） | 引数               | 内容                                                                                                                                                         |
| :--------------- | :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -r               | --recursive        | 再帰的に取得する。ただし、robots.txtで拒否されている場合は、指定したページだけしか取得できない。                                                             |
| -p               | --page-requisites  | ページの表示に必要な画像やcssなどを合わせてダウンロードする。                                                                                                |
| -k               | --convert-links    | ダウンロードしたhtmlファイルからのリンクや画像のパスをうまく表示できるように変換する                                                                         |
| -K               | --backup-converted | .origをつけて変換前のファイルを残す                                                                                                                          |
| -E               | --adjust-extension | mod_rewriteされてたりクエリーストリングによってコンテンツが変わるサイトの場合、.htmlをつけて保存する。古いバージョンのwgetでは--html-extentionだったらしい。 |
| -N               | --timestamping     | ローカルに同名のファイルがあって、ファイルサイズが同じ場合に、更新日時を比較してリモートのほうが新しければダウンロードする。                                 |

## 記事

- [wgetを使用してHTMLファイルのみをダウンロードする方法（画像、CSS、JSを無視する）](https://qastack.jp/superuser/709702/how-to-crawl-using-wget-to-download-only-html-files-ignore-images-css-js)
