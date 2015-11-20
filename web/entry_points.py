import os

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

from web.celery import app


def runner():
    argv = [
        'worker',
        '--loglevel=INFO',
        '-c 1',
    ]
    app.worker_main(argv)


def api():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

    application = get_wsgi_application()
    call_command('runserver', '127.0.0.1:8000')
