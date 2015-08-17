## ObjectSpace

~~~ruby
irb(main):010:0> include ObjectSpace
~~~

~~~ruby
irb(main):037:0> ObjectSpace.each_object(Numeric).to_a
=> [(0+1i), 18446744073709551615, NaN, Infinity, 1.7976931348623157e+308, 2.2250738585072014e-308, 6169619526203342117666908630171183699]
~~~