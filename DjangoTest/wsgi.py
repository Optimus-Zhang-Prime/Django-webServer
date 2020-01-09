"""
WSGI config for DjangoTest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os,sys
sys.path.append('/Django')
sys.path.append('/Django/py3/lib/site-packages')
sys.path.append('/Django/py3/lib64/site-packages')
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoTest.settings')
application = get_wsgi_application()
