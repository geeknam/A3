'''
BASE CLASS SETTINGS FOR ALLOCATE


THESE SETTINGS SHOULD BE GLOBAL TO BE USED REGARDLESS OF ENVIRONMENT
'''

__author__ = 'Warwick'

import os
import sys
import urlparse
import djcelery

class BaseSettings(object):
    #  TODO: THIS WILL BREAK STUFF set the project root
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
    # add custom apps directory at top level to python path to allow access to shit
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

    def project_dir(self, *args):
        if not args[-1] == '' and not args[-1][-1] == '/':
            args = args + ('',)
        return os.path.abspath(os.path.join(self.PROJECT_ROOT, *args))

    @property
    def SITE_ROOT(self):
        return self.project_dir('site_media')

    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    EMAIL_SUBJECT_PREFIX = '[allocate3] '

    ADMINS = [
        ('Jesse O\'Connor', 'jesse@kogan.com.au'),
        ('Nam Ngo Minh', 'nam@kogan.com.au'),
    ]
    MANAGERS = ADMINS
    INTERNAL_IPS = ['127.0.0.1']
    TIME_ZONE = 'Australia/Melbourne'
    LANGUAGE_CODE = 'en-us'

    SITE_ID = 1

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True
    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # redis is needed for some stuff - mainly tracking of task progress to display
    # to use through an ajax call - quicker than writing to db
    REDIS_HOST = 'localhost'    #   default to local redis
    REDIS_PORT = 6379
    REDIS_PASSWORD = None

    SECRET_KEY = 'l^0_bkt75#mxf#)$0ob3xi0!d%vqduj@6e$_72m!@=l71nll-&amp;'

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
    ]


    TEMPLATE_CONTEXT_PROCESSORS = [
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.request",
        "styles.context_processors.styles_classes",
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.static',
        # 'core.context_processors.context',
    ]

    MIDDLEWARE_CLASSES = [
        # 'core.middleware.RedirectSecureMiddleware',
        # 'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.transaction.TransactionMiddleware',
        # 'reversion.middleware.RevisionMiddleware',
        #  'core.middleware.MoveUpURLMiddleware',
        # 'core.middleware.SalesProtectedMiddleware',
        # 'core.middleware.LoginRequiredMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        'styles.middleware.StylesMiddleware',
        'breadcrumbs.middleware.BreadcrumbsMiddleware',
    ]

    KEEP_COMMENTS_ON_MINIFYING = True
    ROOT_URLCONF = 'allocate3.urls'

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = 'allocate3.wsgi.application'

    TEMPLATE_DIRS = [
        os.path.join(PROJECT_ROOT, 'templates'),
    ]

    # GRAPPELLI_INDEX_DASHBOARD = 'allocate3.dashboard.CustomIndexDashboard'
    # GRAPPELLI_ADMIN_TITLE = 'Allocate Site Administration'

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.flatpages',
        # using grappelli with dashboard to provide admin
        # 'grappelli.dashboard',
        # 'grappelli',
        'django.contrib.admin',
        'django.contrib.admindocs',
        'django.contrib.comments',
        'django.contrib.humanize',

        # 'allocate_comments',
        # 'gunicorn',

        # 3rd party requirements
        'south',
        # 'djcelery',
        # 'treemenus',
        'breadcrumbs',
        # 'imagekit',
        # 'compressor',
        'django_extensions',
        # 'reversion',
        # 'import_export',
        'rest_framework',

        # Allocate apps
        'core',
        'suppliers',
        'products',
        'orders',
        # 'bulk_orders',
        # 'payments',
        # 'freight',
        # 'changes',
        # 'emails',
        # 'menu_extensions',
        # 'documents',
        # 'reports',
    ]

    # COMMENTS_APP = 'allocate_comments'

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'console':{
                'level':'INFO',
                'class':'logging.StreamHandler',
                'stream': sys.stdout
            },

            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
                },
            'allocate': {
                'handlers': ['console',],
                'level': 'DEBUG',
                },
            'xhtml2pdf': {
                'handlers': ['console',],
                'level': 'INFO',
                }
        }
    }

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'TIMEOUT': 600,
        }
    }

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = '/media/'

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    @property
    def STATIC_ROOT(self):
        return os.path.join(self.SITE_ROOT, 'static', '')

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'

    ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

    # Additional locations of static files
    @property
    def STATICFILES_DIRS(self):
        return (
             self.project_dir("static"),
        )


    REST_FRAMEWORK = {
        'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
        # Use hyperlinked styles by default.
        # Only used if the `serializer_class` attribute is not set on a view.
        'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',

        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ]
    }

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
        # 'compressor.finders.CompressorFinder',
    )

    # AUTH_PROFILE_MODULE = 'core.UserProfile'

    # list of currencies that should be processed by the payments_currency_sync
    # management command so that we avoid creating excess quoteprice objects for things like
    # mexican peso
    # TODO: use the admin for this instead - download all currencies but restrict creation of
    # TODO: related objects to enabled currencies
    ALLOWED_CURRENCY_CODES = [
        'USD',
        'EUR',
        'AUD',
        'HKD',
        'GBP'
    ]

    # path to the lessc binary so we can compile less to css
    PATH_TO_LESSC = 'lessc'

    def dump(self):
        '''
        copied from K3 =)
        '''
        d = {}
        for k in dir(self):
            if k == k.upper():
                d[k] = getattr(self, k)
        return d

