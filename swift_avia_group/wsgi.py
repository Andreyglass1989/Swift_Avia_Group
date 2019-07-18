"""
WSGI config for swift_avia_group project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swift_avia_group.settings")
sys.path.append('/home/Swift_Avia_Group')
sys.path.append('/home/Swift_Avia_Group/swift_avia_group')

application = get_wsgi_application()