from django.http import HttpResponse
from django.core.files import File
from django.conf import settings
import os
import mimetypes
import re


ROOT = os.path.dirname(
    os.path.dirname(settings.BASE_DIR)).decode('utf8')


def _path(path):
    return os.path.join(ROOT, path)


def publish(request, path):
    if path == '' or path.endswith('/'):
        path = path + "index.md"

    abspath = _path(path)
    mt, dmy = mimetypes.guess_type(abspath)
    return HttpResponse(
        File(open(abspath)), content_type=mt)
