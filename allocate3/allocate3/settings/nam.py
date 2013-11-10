import djcelery
from .base import BaseSettings


class Settings(BaseSettings):
    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'allocate3',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

    @property
    def INSTALLED_APPS(self):
        ia = super(Settings, self).INSTALLED_APPS
        ia += [
            'debug_toolbar',
            'djkombu',     # using kombu as our broker, db-based but okay for this app's size
            # 'devserver',
            'django_nose',
        ]
        return ia

    @property
    def MIDDLEWARE_CLASSES(self):
        mc = super(Settings, self).MIDDLEWARE_CLASSES
        mc += [
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        ]
        return mc

    EMAIL_HOST = 'localhost'
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = 25

    # djcelery.setup_loader()
    # BROKER_BACKEND = 'djkombu.transport.DatabaseTransport'
    # CELERY_RESULT_DBURI = DATABASES['default']

    # COMPRESS_ENABLED = True
    # COMPRESS_PRECOMPILERS = [
    #     ('text/less', '/usr/bin/lessc {infile} {outfile}'),
    # ]

    # COMPRESS_CSS_FILTERS = [
    #     'compressor.filters.css_default.CssAbsoluteFilter',
    #     'compressor.filters.cssmin.CSSMinFilter',
    # ]
    # COMPRESS_JS_FILTERS = [
    #     'compressor.filters.jsmin.JSMinFilter',
    #     'compressor.filters.jsmin.SlimItFilter',
    # ]

    USE_LESS = False

    COMPRESS_HTML = True

    AUTO_ADMIN = True

    SOUTH_TESTS_MIGRATE = False
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

#### DO NOT TOUCH ####
# Extract all the setttings to this file/module's global namespace to be imported
globals().update(Settings().dump())