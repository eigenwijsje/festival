import os 
basedir = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(basedir, 'festival.sqlite')

TIME_ZONE = 'America/La_Paz'

LANGUAGE_CODE = 'es'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(basedir, 'sitemedia')

MEDIA_URL = '/sitemedia/'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'nak8i5g79rxhg0mk7-rzqww59*r7k=x+v-wu)vvt*)=ch-3!50'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'festival.urls'

TEMPLATE_DIRS = (os.path.join(basedir, 'templates'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'installfest',
    'contact_form',
    'registration',
)

ACCOUNT_ACTIVATION_DAYS=7
