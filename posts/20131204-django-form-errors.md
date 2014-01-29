Date: 2013-12-04 08:00
Title: Django:unittestでフォームのエラーをチェックする  
Type: post  
Excerpt:   


Djangoのフォームフィールドのerrorsに、フィールドを示す情報がないので、unittest でBueatifullSoupでチェックできない。ので、 form.afield.errors.as_text をタグで囲む事に。

せっかくなので、Bootstrapのエラーで見栄えを良くするようなテンプレートタグを書くなど(bs.py)。

    # -*- coding: utf-8 -*-
    from django import template
    register = template.Library()

    @register.inclusion_tag('bs/errors.html',takes_context=True)
    def bs_errors(context,field):
        return { 'field': field , }
   

ページテンプレート:

    {% load bs %}
            
    <td> {{ form.usedate}} {% bs_errors form.usedate %} </td>
    
 
インクルージョンタグのテンプレート。alert関係のBootstrapのUI処理をやってくれる:

    {% if field.errors %}
    <div class="alert alert-error">
        <a class="close" data-dismiss="alert" href="#">×</a>
        <span id="error-{{field.auto_id}}">{{ field.errors.as_text }}</span>
    </div>
    {% endif %}    

tests.py:

    from BeautifulSoup import BeautifulSoup as Soup,Tag
    from soupselect import select
    # https://github.com/simonw/soupselect
    
    form  = OrderForm( user=user,id=id)       #:フォームの雛形つくっておいて、
    res = self.post('tickets_order',....)     #:Viewにusedateでエラーが出るようにPOSTした結果
    
    errlist = select( Soup(res.content) ,"span#error-%s" % form['usedate'].auto_id)
    self.assertEqual(len(errlist),1)
    
    