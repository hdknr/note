[jQuery UI spinner](https://jqueryui.com/spinner/)


## HH:MM のスピナー

- `value` を分で持つ( 10:00 は 600 )

~~~js

$.widget( "ui.timespinner", $.ui.spinner, {
    options: { step: 30},
    _parse: function( value ) {
      if ( typeof value === "string" ) {
        if ( Number( value ) == value ) {
          value = Number( value );
        }
        else {
          a = value.split(":").map(function(i) { return Number(i);});
          value = a[0] * 60 + a[1];
        }
      }
      return value;
    },

    _format: function( value ) {
      a0 = Math.floor(value / 60);
      a1 = value % 60;
      return ('00' + a0).substr(-2) + ":" + ('00' + a1).substr(-2);
    }
});
~~~
~~~js
$("#id_open_time").timespinner({min:10 * 60, max:21 * 60, step:30});
~~~
