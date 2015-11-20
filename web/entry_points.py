from web.celery import app


def runner():
    argv = [
        'worker',
        '--loglevel=DEBUG',
    ]
    app.worker_main(argv)
