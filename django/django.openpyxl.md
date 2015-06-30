Django: 指定された条件のレコードをExcelでダウンロードする

- [openpyxl](https://pypi.python.org/pypi/openpyxl)

## ExportQuerySet

~~~~py
from django.db import models
from django.db.models.fields import FieldDoesNotExist
from django.db.models.base import ModelBase

from openpyxl import Workbook
from openpyxl.cell import get_column_letter
from openpyxl.writer import excel

class ExportQuerySet(models.QuerySet):

    def resolve_field_data(self, instance, field):
        path = field.split('.', 1)
        val = getattr(instance, path[0])

        if len(path) > 1 and path[1] != '':
            return self.resolve_field_data(val, path[1])

        try:
            return instance._get_FIELD_display(
                instance._meta.get_field(path[0]))
        except:
            return unicode(val)

    def resolve_field_header(self, model, field, name=''):
        '''
            :param Model model: Model Class
            :param str field: field name path ( i.e) profile.user.username )
            :param unicode name: resolved name path prefix
        '''
        path = field.split('.', 1)
        try:
            field = model._meta.get_field(path[0])
            name = (name and name + '.' or '') + unicode(
                field.verbose_name)
        except FieldDoesNotExist:
            field = getattr(model, path[0]).related.model
            name = (name and name + '.' or '') + unicode(
                field._meta.verbose_name)

        if len(path) > 1 and path[1] != '':
            next_model = issubclass(
                type(field), ModelBase
            ) and field or field.rel.to
            return self.resolve_field_header(next_model, path[1], name)

        return name

    def create_xlsx(self, wb=None, excludes=[], relations=[]):
        wb = wb or Workbook()
        ws = wb.create_sheet(0)

        ws.title = unicode(self.model._meta.verbose_name)

        names = tuple(
            (field.name, ugettext(field.verbose_name))
            for field in self.model._meta.fields
            if field.name not in excludes
        ) + tuple(
            (field, self.resolve_field_header(self.model, field))
            for field in relations
        )

        # Header
        row = 1
        for col in xrange(1, len(names) + 1):
            value = names[col - 1][1]
            cl = get_column_letter(col)
            ws.cell('%s%d' % (cl, row)).value = value
            
        # Records
        for obj in self.filter():
            row = row + 1
            for col in xrange(1, len(names) + 1):
                colname = names[col - 1][0]
                if colname.find('.') >= 0:
                    value = self.resolve_field_data(obj, colname)
                else:
                    value = obj._get_FIELD_display(
                        obj._meta.get_field(colname))

                if isinstance(value, unicode) and len(value) > 0:
                    value = gettext(value)

                cl = get_column_letter(col)
                ws.cell('%s%d' % (cl, row)).value = value

        return wb

    def export_xlsx(self, output=None, wb=None, excludes=[], relations=[],
                    *args, **kwargs):

        xlsx = self.create_xlsx(wb, excludes=excludes, relations=relations)

        if output is None:
            return xlsx

        if isinstance(output, basestring):
            return excel.save_workbook(xlsx, output)

        if issubclass(output, HttpResponse):
            res = output(excel.save_virtual_workbook(xlsx),
                         content_type='application/vnd.ms-excel',
                         *args, **kwargs)
            res['Content-Disposition'] = \
                'attachment; filename={0}.xlsx'.format(
                    self.model._meta.verbose_name.encode('utf8'))
            return res

        return xlsx
~~~

## Order

~~~py

class Order(models.Model):
	ticket = models.ForeignKey(Ticket, verbose_name=_('Ticket'))
	user = models.ForeignKey(User, verbose_name=_('User'))
	
    # Managers
    objects = OrderManager()
    exports = ExportQuerySet.as_manager()

~~~

## order_download

- 指定されたTicketの指定された期間に注文されたOrderをダウンロードする

~~~py
@staff_member_required
def order_download(request, id, status=None):
    ticket = Ticket.objects.get(id=id)
    
    q = {}    
    df = request.GET.get('df', None)
    dt = request.GET.get('dt', None)
    _tz = get_default_timezone()
    if df: 
        q['created_at__gte'] = make_aware(
            datetime.strptime(df, '%Y-%m-%d'), _tz)
    if dt: 
        q['created_at__lte'] = make_aware(
            datetime.strptime(dt, '%Y-%m-%d'), _tz)

    return ticket.order_set(
        manager='exports'
    ).filter(**q).export_xlsx(
        HttpResponse,
        excludes=['signature'],
        relations=['user.profile'],
    ) 
~~~    
