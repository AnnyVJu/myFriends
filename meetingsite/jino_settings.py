import os

STATIC_ROOT = os.path.join(os.path.expanduser('~'), 'domains/net.njay.ru/static/')
MEDIA_ROOT = os.path.join(os.path.expanduser('~'), 'domains/net.njay.ru/media/')

DEBUG = False

ALLOWED_HOSTS = ['*']
