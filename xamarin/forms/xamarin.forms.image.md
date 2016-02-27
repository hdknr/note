
- [Universal Image Loader](https://components.xamarin.com/gettingstarted/universalimageloader)
- Android: [Xamarin.Forms イメージ](http://dev.classmethod.jp/smartphone/xamarin-forms-image/)

## UriImageSource
- [Working with Images](https://developer.xamarin.com/guides/xamarin-forms/working-with/images/)
- [Xamarin.Forms.UriImageSource Class](https://developer.xamarin.com/api/type/Xamarin.Forms.UriImageSource/)
- [Clear image cache](https://forums.xamarin.com/discussion/26773/clear-image-cache)
- [Image Cache Location](https://forums.xamarin.com/discussion/32369/image-cache-location)
- [Xamarin Tips and Tricks #1 – UriImageSource](http://www.itworksonmymachine.net/index.php/2015/04/02/xamarin-tips-and-tricks-1-uriimagesource/)



~~~
$ adb devices

List of devices attached
emulator-5554   device
10.71.34.101:5555       device
356592050465307 device


$ export DROID_DEVICE=356592050465307

$ adb -s ${DROID_DEVICE} shell

shell@SH-06F:/ $ run-as jp.lafoglia.mobilecache
shell@SH-06F:/data/data $ cd files/.config/.isolated-storage/                                          
shell@SH-06F:/data/data/jp.lafoglia.mobilecache/files/.config/.isolated-storage $

shell@SH-06F:/data/data/jp.lafoglia.mobilecache/files/.config/.isolated-storage $ ls -al
drwx------ u0_a437  u0_a437           2016-02-20 14:40 ImageLoaderCache
-rw------- u0_a437  u0_a437       137 2016-02-20 14:40 PropertyStore.forms

shell@SH-06F:/data/data/jp.lafoglia.mobilecache/files/.config/.isolated-storage $ ls -l ImageLoaderCache
-rw------- u0_a437  u0_a437     36147 2016-02-20 14:40 537b0acf4c00724271053e63721be40e

~~~


## AsyncImageSource

~~~csharp
public static class AsyncImageSource
{
    public static NotifyTaskCompletion<ImageSource> FromTask(Task<ImageSource> task, ImageSource defaultSource)
    {
        return new NotifyTaskCompletion<ImageSource>(task, defaultSource);
    }

    public static NotifyTaskCompletion<ImageSource> FromUriAndResource(string uri, string resource)
    {
        var u = new Uri(uri);
        return FromUriAndResource(u, resource);
    }

    public static NotifyTaskCompletion<ImageSource> FromUriAndResource(Uri uri, string resource)
    {
        var t = Task.Run(() => ImageSource.FromUri(uri));
        var defaultResouce = ImageSource.FromResource(resource);

        return FromTask(t, defaultResouce);
    }
}
~~~


## FFImageLoading

- https://github.com/molinch/FFImageLoading


- UICollectionViewCell にイメージを表示させる

~~~csharp

using System;

using Foundation;
using UIKit;
using FFImageLoading;
using FFImageLoading.Work;
using FFImageLoading.Transformations;

namespace Simple.iOS.Sample
{
    public partial class ImageViewCell : UICollectionViewCell
    {
        public static readonly NSString Key = new NSString("ImageViewCell");

        private string _imageURL;
        public string imageURL
        {
            set
            {
                if(value!=_imageURL)
                {
                    _imageURL = value;
                    UpdateContent();
                }                
            }
            get { return _imageURL; }
        }

        protected void UpdateContent()
        {
            ImageService.LoadUrl(imageURL)
                        .ErrorPlaceholder("error@2x.png", ImageSource.ApplicationBundle)
                        .LoadingPlaceholder("placeholder.png", ImageSource.CompiledResource)
                        .Into(imageView);            
        }
    }
}
~~~

- キャッシュを取り消す

~~~csharp

using Foundation;
using System.CodeDom.Compiler;

namespace Simple.iOS.Sample
{
	[Register ("ImagesViewController")]
	partial class ImagesViewController
	{
		[Action ("TapReloadAll:")]
		partial void TapReloadAll (Foundation.NSObject sender);
	}
}

using System;

using UIKit;
using Foundation;
using FFImageLoading;

namespace Simple.iOS.Sample
{
    public partial class ImagesViewController : UICollectionViewController
    {
        partial void TapReloadAll (Foundation.NSObject sender)
        {
            FFImageLoading.ImageService.InvalidateMemoryCache();
            FFImageLoading.ImageService.InvalidateDiskCache();
            CollectionView.ReloadData();
        }
    }
}
~~~

- 変換

~~~csharp
using System;

using UIKit;

using FFImageLoading;
using FFImageLoading.Work;
using FFImageLoading.Transformations;

namespace Simple.iOS.Sample
{
    public partial class ImageDetailsViewController : UIViewController
    {
        public const string SegueImageDetails = "ImageDetails-segue";

        public string imageURL = string.Empty;

        public override void ViewWillAppear(bool animated)
        {
            base.ViewWillAppear(animated);
            transformation = 0;
            LoadImage();
        }

        int transformation = 0;

        protected void LoadImage()
        {
            var taskImage = ImageService.LoadUrl(imageURL)
                .ErrorPlaceholder("error@2x.png", ImageSource.ApplicationBundle)
                .LoadingPlaceholder("placeholder.png", ImageSource.CompiledResource);
            if(transformation==0)
            {                
                taskImage.Into(imageView);
                transformation++;
            }
            else if(transformation==1)
            {
                taskImage.Transform(new CircleTransformation())                
                         .Into(imageView);
                transformation++;
            }
            else if(transformation==2)
            {
                taskImage.Transform(new RoundedTransformation(10))                
                         .Into(imageView);
                transformation = 0;
            }
        }

        // タップしたときのハンドラ
        partial void TapTransformation (Foundation.NSObject sender)
        {
            LoadImage();
        }
    }
}
~~~
