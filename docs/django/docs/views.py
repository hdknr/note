from django.http import HttpResponse
from django.core.files import File
from django.conf import settings
import os
import mimetypes
import re
from markdown import Markdown
import traceback


ROOT = os.path.dirname(
    os.path.dirname(settings.BASE_DIR)).decode('utf8')
MD = Markdown(
        extensions=[u'meta', u'toc', u'tables', u'fenced_code'], 
        extension_configs={})

def _path(path):
    return os.path.join(ROOT, path)


def publish(request, path):
    if path == '' or path.endswith('/'):
        path = path + "index.md"

    abspath = _path(path)
    mt, dmy = mimetypes.guess_type(abspath)
    mt = mt or os.path.splitext(path)[1]
    try:
        source = File(open(abspath))
        if mt == ".md":
            return HttpResponse(
                MD.convert(source.read().decode('utf8')))
        return HttpResponse(
                source, content_type=mt)
    except:
        print traceback.format_exc()
        return HttpResponse()
