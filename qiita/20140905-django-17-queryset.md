Django 1.7:リリースノート: モデルマネージャ関連


# QuerySet.as_manager() #

- https://docs.djangoproject.com/en/dev/releases/1.7/#calling-custom-queryset-methods-from-the-manager

Managerインスタンスを返すので、
Managerクラスを定義しなくても良くなった:

    The QuerySet.as_manager() class method can now directly create Manager 
    with QuerySet methods:

        class FoodQuerySet(models.QuerySet):
            def pizzas(self):
                return self.filter(kind='pizza')
        
            def vegetarian(self):
                return self.filter(vegetarian=True)
        
        class Food(models.Model):
            kind = models.CharField(max_length=50)
            vegetarian = models.BooleanField(default=False)
            objects = FoodQuerySet.as_manager()
        
        Food.objects.pizzas().vegetarian()

[as_manager()ソース](https://github.com/django/django/blob/master/django/db/models/query.py#L66):

    def as_manager(cls):
        # Address the circular dependency between `Queryset` and `Manager`.
        from django.db.models.manager import Manager
        return Manager.from_queryset(cls)()
 
    as_manager = classmethod(as_manager)


[from_querset()ソース](https://github.com/django/django/blob/master/django/db/models/manager.py#L106):

    @classmethod
    def from_queryset(cls, queryset_class, class_name=None):
        if class_name is None:
            class_name = '%sFrom%s' % (cls.__name__, queryset_class.__name__)
        class_dict = { 
            '_queryset_class': queryset_class,
        }   
        class_dict.update(cls._get_queryset_methods(queryset_class))
        return type(class_name, (cls,), class_dict)


サンプル:

    class TodoQuerySet(models.QuerySet):
        def open_items(self):
            return self.filter(closed=False)
    
        def high_priority_items(self):
            return self.filter(
                priority=self.model.PRIORITY_HIGH)
    
        def important_items(self):
            return self.open_items().high_priority_items()

     class Todo(models.Model):
         # ....
         objects = TodoQuerySet.as_manager()
     
    >>> from tods.models import *
    >>> TodoQuerySet.as_manager()
    <django.utils.deprecation.ManagerFromTodoQuerySet object at 0x34d31d0>
    >>> m = _
    
    >>> m.__class__.__name__
    'ManagerFromTodoQuerySet' 

    >>> m._queryset_class
    <class 'todos.models.TodoQuerySet'>

    >>> m.model == None
    True

    >>> Todo.objects.model
    <class 'todos.models.Todo'>


1.6だったら:

    from django.db.models.query import QuerySet

    class TodoMethods(object):
        ''' 
            - メソッドを用意した mixin を定義
            - QuerySet, Managerにmixinする
        '''
        def open_items(self):
            return self.filter(closed=False)

        def high_priority_items(self):
            return self.filter(
                priority=self.model.PRIORITY_HIGH)

        def important_items(self):
            return self.open_items().high_priority_items()

    class TodoQuerySet(QuerySet, TodoMethods):
        pass

    class TodoManager(models.Manager, TodoMethods):
        def get_queryset(self):
            ''' QuerySetを返す '''
            return TodoQuerySet(self.model, using=self._db)

     class Todo(models.Model):
         # ....
         objects = TodoManager()


# 逆参照のクエリにマネージャを名前で指定できるようになった#

- https://docs.djangoproject.com/en/dev/releases/1.7/#using-a-custom-manager-when-traversing-reverse-relations

リリースノート:

    class Blog(models.Model):
        pass
    
    class Entry(models.Model):
        blog = models.ForeignKey(Blog)
    
        objects = models.Manager()  # Default Manager
        entries = EntryManager()    # Custom Manager
    
    b = Blog.objects.get(id=1)
    b.entry_set(manager='entries').all()


# Prefechオブジェクト # 

- https://docs.djangoproject.com/en/dev/releases/1.7/#new-prefetch-object-for-advanced-prefetch-related-operations
- [Prefech オブジェクト](https://docs.djangoproject.com/en/dev/ref/models/queries/#django.db.models.Prefetch)
  が定義されたので、これを使って
  [prefech_related](https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.prefetch_related)を細かく制御できます。
- リレーションのフィルタリング、 
  プリフェッチしたレリレーションの[select_related](https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.select_related)の呼び出し、 クエリセットが違ってもリレーションが同じであればプリフェッチで効率化できるとか。



# DBカーソルコンテキストマネージャ #

- https://docs.djangoproject.com/en/dev/releases/1.7/#using-database-cursors-as-context-managers

with使えるようになった:

    with connection.cursor() as c:
        c.execute(...)

# カスタムルックアップ #

- https://docs.djangoproject.com/en/dev/releases/1.7/#custom-lookups

Custom lookups
It is now possible to write custom lookups and transforms for the ORM. Custom lookups work just like Django’s inbuilt lookups (e.g. lte, icontains) while transforms are a new concept.

The django.db.models.Lookup class provides a way to add lookup operators for model fields. As an example it is possible to add day_lte operator for DateFields.

The django.db.models.Transform class allows transformations of database values prior to the final lookup. For example it is possible to write a year transform that extracts year from the field’s value. Transforms allow for chaining. After the year transform has been added to DateField it is possible to filter on the transformed value, for example qs.filter(author__birthdate__year__lte=1981).

For more information about both custom lookups and transforms refer to the custom lookups documentation.


jjj