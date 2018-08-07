## navbar

- Bulma は Javascript が用意されていないので、ハンバーガーメニューの表示/非表示の処理を自分でやる必要がある

Javascript:

~~~js
document.addEventListener('DOMContentLoaded', function () {
  // "navbar-burger" 要素
  var $navbarBurgers = Array.prototype.slice.call(
        document.querySelectorAll('.navbar-burger'), 0);
  
  // navbar-burger が存在したら
  if ($navbarBurgers.length > 0) {
  
    // それぞれにクリックイベント を
    $navbarBurgers.forEach(function ($el) {
      $el.addEventListener('click', function () {
        // data-target (メニュー)を取得
        var target = $el.dataset.target;
        var $target = document.getElementById(target);
  
        $el.classList.toggle('is-active');          // ハンバーガーボタンをトグル
        $target.classList.toggle('is-active');      // メニューをトグル
      });
    });
  }
  
});
~~~

vue.js:

~~~html
  <nav class="navbar" role="navigation" aria-label="main navigation">
            <div class="navbar-brand">
                <a class="navbar-item" href="#">
                    <img src="{% static 'site/img/logo.png' %}" alt="allfoods: Local foods for everyone" width="100" height="42">
                </a>
            
                <div role="button" 
                    @click="toggleNavMenu"
                    :class="{'is-active': navIsActive}"
                    class="navbar-burger" 
                    data-target="nav-menu" aria-label="menu" aria-expanded="false">
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </div>
            </div>

            <div :class="{'is-active': navIsActive}" class="navbar-menu"  id="nav-menu" >
                <div class="navbar-start">
                    <a class="navbar-item" href="#">About</a>
                </div>
                
                <div class="navbar-end">
                    <a class="navbar-item" href="#">Help</a>
                </div>
            </div>
        </nav>