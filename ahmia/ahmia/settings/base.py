"""Django project settings for ahmia."""
from os.path import dirname, join, abspath

from decouple import config, Csv


# Set the PROJECT_HOME variable.
# This will be used to prepend to all file/directory paths.
PROJECT_HOME = abspath(join(dirname(__file__), '..', '..'))

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# ELASTICSEARCH STUFF
ELASTICSEARCH_TLS_FPRINT = config(
    'ELASTICSEARCH_TLS_FPRINT',
    default="8C:DC:67:EA:C3:B3:97:94:92:30:81:35:8C:C6:D9:2A:E2:E6:8E:3E")
# 'https://ahmia.fi/esconnection/'
ELASTICSEARCH_SERVERS = config('ELASTICSEARCH_SERVERS', default='http://localhost:9200')
ELASTICSEARCH_INDEX = config('ELASTICSEARCH_INDEX', default='latest-crawl')
ELASTICSEARCH_TYPE = config('ELASTICSEARCH_TYPE', default='tor')

# Email settings
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=587)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default="example@lol.fi")
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default="well_I_am_not_pushing_it_to_git")
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default=EMAIL_HOST_USER)
RECIPIENT_LIST = config('RECIPIENT_LIST', cast=Csv(), default=DEFAULT_FROM_EMAIL)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

STATIC_URL = '/static/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# todo STATIC_ROOT should be project-level, not app-level, or?
STATIC_ROOT = join(PROJECT_HOME, 'ahmia/static/')

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = config('SECRET_KEY', default='%*ertqgmh3(t_d=i&ojuc!02wnech_nq#1*s7dbv3h=&ruf7*b')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'ahmia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'ahmia',
    'search',
    'stats'
)
