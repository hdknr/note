from django.db import models
from django.utils.translation import (
    ugettext_lazy as _,
)
from django.conf import settings
import os
import hashlib
import mimetypes


def _create_upload_path(self, filename):
    self.filename = filename.encode('utf8')
    self.ext = os.path.splitext(self.filename)[1].lower()

    newfilename = "%s/%s/%s%s" % (
        self._meta.app_label,
        self._meta.model_name,
        hashlib.md5(self.filename).hexdigest(),
        self.ext,
    )

    if os.path.isfile(os.path.join(settings.MEDIA_ROOT, newfilename)):
        os.remove(os.path.join(settings.MEDIA_ROOT, newfilename))
    return newfilename


class AbstractMediaFile(models.Model):

    data = models.FileField(
        _(u'Data File'),
        upload_to=_create_upload_path)

    filename = models.CharField(
        _(u'File Name'),
        max_length=200, null=True, blank=True, default=None)

    ext = models.CharField(
        _(u'File Extension'), max_length=10,
        db_index=True, default='', blank=True, )

    @property
    def miemtype(self):
        return mimetypes.guess_type(self.filename)[0]

    def response(self, response_class, meta=False):
        res = response_class(self.data, content_type=self.mimetype)
        if meta:
            res['Content-Disposition'] = 'attachment; filename=%s' % (
                os.path.basename(self.data.name)
            )
        return res

    class Meta:
        abstract = True


class DataFile(AbstractMediaFile):
    description = models.TextField(null=True)
    created_at = models.DateTimeField(_(u'Created At'), auto_now_add=True, )
    updated_at = models.DateTimeField(_(u'Updated At'), auto_now=True, )
