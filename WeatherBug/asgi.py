"""
ASGI config for WeatherBug project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherBug.settings')

application = get_asgi_application()
