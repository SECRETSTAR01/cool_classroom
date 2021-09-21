'''Use this for production'''

from .base import *

DEBUG = True
ALLOWED_HOSTS += ['http://domain.com']
WSGI_APPLICATION = 'home.wsgi.prod.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# import dj_database_url
# dj_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "d69hv490qgcrt4",
        "USER": "otjsxwiagrdpiq",
        "PASSWORD": "d2afc4dba0c4c86f66f829af51d0329d06bf41e519105fc48b6ff6560fee8248",
        "HOST": "ec2-54-158-247-97.compute-1.amazonaws.com",
        "PORT": "5432",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
