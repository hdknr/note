- [Ruby and Python by Example](http://grschafer.com/guides/2013/08/20/ruby-and-python-by-example/)c


## dir(obj)

- dir(something) のワンライナー

~~~
def dir(object) print object.methods.sort.join("\n").to_s end
~~~

## dir()

- [local_variables](http://ruby-doc.org/core-2.2.0/Kernel.html#method-i-local_variables)

~~~ruby
$ irb
irb(main):001:0> local_variables
=> [:_]

irb(main):002:0> _
=> [:_]

irb(main):003:0> a = 3
=> 3
irb(main):004:0> b = 4
=> 4
irb(main):005:0> local_variables
=> [:b, :a, :_]

irb(main):006:0> b
=> 4
irb(main):007:0> a
=> 3

~~~

- クラス数

~~~ruby
irb(main):019:0> ObjectSpace.each_object(Class).count
=> 453
~~~

- クラス名に 'Cat' を含む一覧

~~~
irb(main):018:0> ObjectSpace.each_object(Class){|c| p c if c.name.include?('Cat')}
Zoo::Cat
Cat
=> 453
~~~

- instance_methods

~~~
irb(main):008:0> instance_methods
NameError: undefined local variable or method `instance_methods' for main:Object
	from (irb):8
	from /home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/bin/irb:11:in `<main>'
~~~