- http://sstut.com/csharpdotnet/javascript-timers-equivalent.php


~~~csharp

System.Threading.Tasks
  .Task.Delay(System.TimeSpan.FromSeconds(3.0))
    .ContinueWith((task)=>{ System.Console.WriteLine("aaa");});
~~~    
