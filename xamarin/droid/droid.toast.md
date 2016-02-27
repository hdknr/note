- http://stackoverflow.com/questions/3134683/android-toast-in-a-thread

~~~csharp
 string t = "msg";
 Android.Widget.Toast.MakeText(
  this, t, Android.Widget.ToastLength.Short).Show();
~~~
