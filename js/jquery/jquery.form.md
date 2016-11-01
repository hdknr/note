
## submit

- [Jquery function BEFORE form submission](http://stackoverflow.com/questions/21938788/jquery-function-before-form-submission)

~~~javascript
$("#search-form").submit(function(){
    if( invalid )
      return false;   // 送信しない
});
~~~

## フォームが空？

- [Checking if ALL form inputs are empty with jQuery](http://stackoverflow.com/questions/10517315/checking-if-all-form-inputs-are-empty-with-jquery)

- `ex` のフィールド以外がすべて空だったら `submit` しない

~~~js
$("#search-form").submit(function(){
       var ex =  ["gender_opt"];
       return  $(this).serializeArray().filter(
         function(e){
          return e.value != '' && e.value != null && ex.indexOf(e.name) < 0; }
        ).length > 0;
   });
~~~   
