# Promise

## 複数のPromis を待つ

~~~js
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

function get_ticketorder_list(){
    return axios.get('/tickets/api/ticketorder/');
}
function patch_ticketorder(ticketorder){
    var url = '/tickets/api/ticketorder/' + ticketorder.id + '/';
    console.log(url)
    return axios.patch(url, ticketorder);
}
~~~

~~~js
    get_ticketorder_list().then(function(res){
        var promises = _.map(res.data, function(obj){
          obj.remarks = obj.remarks + '***';
          return patch_ticketorder(obj);
        });

        axios.all(promises).then(function(res) {
          var results = _.map(res, function(r){
            return r.data;
          });
          console.log(results);
        });
    });
~~~