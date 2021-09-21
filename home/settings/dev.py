'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = True

WSGI_APPLICATION = 'home.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

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

# import dj_database_url
# dj_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(dj_from_env)

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000', 'http://127.0.0.1:8000'
)