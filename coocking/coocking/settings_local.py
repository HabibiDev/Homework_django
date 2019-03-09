import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

<<<<<<< HEAD
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'postgres',
       'USER': 'postgres',
       'PASSWORD': '123',
       'HOST': '172.17.0.4',
       'PORT': '5432'
   }
}

INTERNAL_IPS = '172.17.0.4'
=======
DATABASES = {  
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_ENV_DB', 'postgres'),
        'USER': os.environ.get('DB_ENV_POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_ENV_POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DB_PORT_5432_TCP_ADDR', 'db'),
        'PORT': os.environ.get('DB_PORT_5432_TCP_PORT', ''),
    },
}


REDIS_PORT = 6379  
REDIS_DB = 0  
REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', 'redis')
>>>>>>> 7b67b6bb20835b3bb63127c0f95e148f5b77929e
