Django: msgfmt するまえに msgcat させる

- `django makemessages` で pyファイルから生成した django.poのほかに、手動で定義した po ファイルも使いたい。
- `django.utils.translation.ugettext` に変数を渡す場合もあるので。

~~~
$ tree locale/
locale/
└── ja
    └── LC_MESSAGES
        ├── django.mo
        ├── django.po
        └── imports.po
~~~

# cmsgs.py 

- Django の compilemessages をカスタマイズ
- `python manage.py cmsgs` すると LC_MESSAGES以下の po ファイルをマージしてからmsgfmtします。

~~~python

from __future__ import unicode_literals

# import codecs
import glob
import os

from django.core.management.base import CommandError
from django.core.management.utils import find_command, popen_wrapper
from django.utils._os import upath
from django.core.management.commands.compilemessages import (
    Command as CompileCommand
)


class Command(CompileCommand):

    def handle(self, **options):
        locale = options.get('locale')
        exclude = options.get('exclude')
        self.verbosity = int(options.get('verbosity'))
        if options.get('fuzzy'):
            self.program_options = self.program_options + ['-f']

        if find_command(self.program) is None:
            raise CommandError("Can't find %s. Make sure you have GNU gettext "
                               "tools 0.15 or newer installed." % self.program)

        basedirs = [os.path.join('conf', 'locale'), 'locale']
        if os.environ.get('DJANGO_SETTINGS_MODULE'):
            from django.conf import settings
            basedirs.extend(upath(path) for path in settings.LOCALE_PATHS)

        # Gather existing directories.
        basedirs = set(map(os.path.abspath, filter(os.path.isdir, basedirs)))

        if not basedirs:
            raise CommandError("This script should be run from the Django Git "
                               "checkout or your project or app tree, or with "
                               "the settings module specified.")

        # Build locale list
        all_locales = []
        for basedir in basedirs:
            locale_dirs = filter(os.path.isdir, glob.glob('%s/*' % basedir))
            all_locales.extend(map(os.path.basename, locale_dirs))

        # Account for excluded locales
        locales = locale or all_locales
        locales = set(locales) - set(exclude)

        for basedir in basedirs:
            if locales:
                dirs = [os.path.join(basedir, l, 'LC_MESSAGES')
                        for l in locales]
            else:
                dirs = [basedir]
                
		    # ここより上はcompilemsssages.py と同じ
      		for i in dirs:
                self.merge_and_compile_messages(i)

    def merge_and_compile_messages(self, msgdir):                                   
        src = os.path.join(msgdir, '.po')                                     
        dst = os.path.join(msgdir, 'django.mo')                                     
        pos = [os.path.join(msgdir, f) for f in glob.glob1(msgdir, '*.po')]         
        self.run(['msgcat', '--use-first', '-o', src] + pos)                        
        self.run([self.program] + self.program_options +                            
                 ['--use-fuzzy', '-o', dst, src])                                   
        self.run(['rm', src]) 

    def run(self, args):
        output, errors, status = popen_wrapper(args)
        if not status:
            return

        msg = "Execution of {0} failed: {1}".format(args[0], errors or '')
        raise CommandError(msg)
~~~
