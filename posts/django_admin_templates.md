Date: 2013-06-21
Title: Grappelli の Admin テンプレート修正

* Django Admin のテンプレートは必要なファイルだけカスタマイズできるようになっている。
* [Grappelli](https://github.com/sehmaschine/django-grappelli) のテンプレートも同じルールでカスタマイズされている。
* いくつか足りないところがあるので修正してみた。

### Django Admin Templates ###

    ../../lib/python2.7/site-packages/django/contrib/admin/templates/
    ├── admin
    │   ├── 404.html
    │   ├── 500.html
    │   ├── actions.html
    │   ├── app_index.html
    │   ├── auth
    │   │   └── user
    │   │       ├── add_form.html
    │   │       └── change_password.html
    │   ├── base.html
    │   ├── base_site.html
    │   ├── change_form.html
    │   ├── change_list.html
    │   ├── change_list_results.html
    │   ├── date_hierarchy.html
    │   ├── delete_confirmation.html
    │   ├── delete_selected_confirmation.html
    │   ├── edit_inline
    │   │   ├── stacked.html
    │   │   └── tabular.html
    │   ├── filter.html
    │   ├── includes
    │   │   └── fieldset.html
    │   ├── index.html
    │   ├── invalid_setup.html
    │   ├── login.html
    │   ├── object_history.html
    │   ├── pagination.html
    │   ├── prepopulated_fields_js.html
    │   ├── search_form.html
    │   └── submit_line.html
    └── registration
        ├── logged_out.html
        ├── password_change_done.html
        ├── password_change_form.html
        ├── password_reset_complete.html
        ├── password_reset_confirm.html
        ├── password_reset_done.html
        ├── password_reset_email.html
        └── password_reset_form.html

### 拡張 ###
テンプレートローダーが見つけられるディレクトリにテンプレートファイルを置くとそれを優先してくれる。
例えば、

    app/templates/admin/
    ├── app_index.html
    ├── change_form.html
    ├── change_list.html
    ├── index.html
    ├── readme.rst
    └── reference_models.html
    
だと、index.html, app_index.html change_form.html,change_list.html がDjangoのAdminが用意したそのファイルより優先で呼ばれる。

さらに、{{ アプリケーションラベル }}/{{ モデル名 }} でサブディレクトリを作ると、モデル毎にカスタマイズ出来るようになっている。

### Grappelli ###

Grappelli もこのルールでDjango Admin テンプレートを拡張している。

    ../grappelli/grappelli/templates/admin
    ├── 404.html
    ├── 500.html
    ├── actions.html
    ├── app_index.html
    ├── auth
    │   └── user
    │       ├── add_form.html
    │       └── change_password.html
    ├── base.html
    ├── base_site.html
    ├── change_form.html
    ├── change_list.html
    ├── change_list_filter_sidebar.html
    ├── change_list_results.html
    ├── csv_export_selected_confirmation.html
    ├── date_hierarchy.html
    ├── delete_confirmation.html
    ├── delete_selected_confirmation.html
    ├── edit_inline
    │   ├── stacked.html
    │   └── tabular.html
    ├── filter.html
    ├── filter_listing.html
    ├── includes
    │   ├── fieldset.html
    │   └── fieldset_inline.html
    ├── includes_grappelli
    │   └── header.html
    ├── index.html
    ├── invalid_setup.html
    ├── login.html
    ├── object_history.html
    ├── pagination.html
    ├── prepopulated_fields_js.html
    ├── search_form.html
    ├── submit_line.html
    └── template_validator.html

### grappelli/templates/admin/change_form.htm ###

パン屑のアプリ名が多国語対応がうまく行っていない気がする。

    <!-- BREADCRUMBS --> 
    {% block breadcrumbs %}
        {% if not is_popup %}
            <ul>
                <li><a href="../../../">{% trans "Home" %}</a></li>
                <li><a href="../../">{% trans app_label|capfirst|escape %}</a></li>
                <li>{% if has_change_permission %}<a href="../">{{ opts.verbose_name_plural|capfirst }}</a>{% else %}{{ opts.verbose_name_plural|capfirst }}{% endif %}</li> 
                <li>{% if add %}{% trans "Add" %} {{ opts.verbose_name }}{% else %}{{ original|truncatewords:"18" }}{% endif %}</li>
            </ul>
        {% endif %}
    {% endblock %}

#### app/templates/admin/change_form.html ####    		
* ので、アプリのGrappelliからコピってアプリのchange_form.html を作る
* {% with as %} {% endwith %} でローカル変数を trans するようにする。

このような感じ。

    <!-- BREADCRUMBS --> 
    {% block breadcrumbs %}
        {% if not is_popup %}
            <ul>
                <li><a href="../../../">{% trans "Home" %}</a></li>
                {% with app_label|capfirst|escape as app_label_escaped %}
                <li><a href="../../">{% trans app_label_escaped %}</a></li>
                {% endwith %}
                <li>{% if has_change_permission %}<a href="../">{{ opts.verbose_name_plural|capfirst }}</a>{% else %}{{ opts.verbose_name_plural|capfirst }}{% endif %}</li> 
                <li>{% if add %}{% trans "Add" %} {{ opts.verbose_name }}{% else %}{{ original|truncatewords:"18" }}{% endif %}</li>
            </ul>
        {% endif %}
    {% endblock %}

* 同じように別のファイルも対応すればよい。

### django.contrib.auth.models.User の多国語 ###

* AbstractUserには Meta: verbose_name(_plural)は定義されているので、多国語表示できる。
* が、サブクラスのUserには定義されていない。
* 面倒くさいから、直接編集する。

これ。

    class User(AbstractUser):
        """
        Users within the Django authentication system are represented by this
        model.

        Username, password and email are required. Other fields are optional.
        """
        class Meta:
            swappable = 'AUTH_USER_MODEL'
            verbose_name = _('user')			#: 追加
            verbose_name_plural = _('users')	#: 追加
            