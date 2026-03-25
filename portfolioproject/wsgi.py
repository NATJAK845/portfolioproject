"""
WSGI config for portfolioproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""
import os
import sys

project_home = '/home/NathanielZaneJakosalem/portfolioproject'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolioproject.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()