~~~csharp
> using System.Collections.Generic;
> var q = new Queue<int>();
> q.Enqueue(1)
> q.Enqueue(2)
> q.Enqueue(3)
> q
[
1,
2,
3
]
~~~

~~~csharp
> q.Dequeue()
1
> q
[
  2,
  3
]
~~~

~~~csharp
> q.Count()
7
~~~

## 最後の処理だけ

~~~
using System.Collections.Generic;
using System.Threading;

var queue = new Queue<int>();

for(var i=0; i < 5 ; i++){

    Console.WriteLine("{0} {1}", DateTime.Now.ToLongTimeString(),  i);
    queue.Enqueue(i);

    System.Threading.Tasks
      .Task.Delay(System.TimeSpan.FromSeconds(3.0))
        .ContinueWith(
            (task)=>{
                var v = queue.Dequeue();
                if(queue.Count() > 0){
                    Console.WriteLine("Skipping {0} {1}",
                        v, DateTime.Now.ToLongTimeString());
                }
                else{
                    Console.WriteLine("The Last one {0} {1}",
                        v, DateTime.Now.ToLongTimeString());
                }
            }
        );
    Thread.Sleep(2000);
}

var c = Console.Read();
~~~
