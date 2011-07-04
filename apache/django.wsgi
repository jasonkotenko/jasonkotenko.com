import os
import sys

path = '/home/jason/'
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'jasonkotenko.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()