"""
Django settings for coffeehouse project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os
from dotenv import load_dotenv
import socket


load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# If the host name starts with 'li', set LIVEHOST = True
if socket.gethostname().startswith('li'):
    LIVEHOST = True
else:
    LIVEHOST = False

# Define general behavior variables for live host and non-live host
if LIVEHOST:
    DEBUG = False
else:
    DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^9ze(b)@e20a-c!cferimw+h0+=bva0g4k=l3w(_ed00am@yio'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'coffeehouse.about',
    'coffeehouse.stores',
    'coffeehouse.drinks',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'coffeehouse.urls'

TEMPLATES = [
    { 
        'BACKEND':'django.template.backends.jinja2.Jinja2',
        'DIRS': ['%s/templates/'% (PROJECT_DIR),],
        'APP_DIRS': True,
        'OPTIONS': { 
            'extensions': [
                'jdj_tags.extensions.DjangoCompat',
                'coffeehouse.jinja.extensions.DjangoNow'
                ],
            'environment': 'coffeehouse.jinja.env.JinjaEnvironment'
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['%s/templates/'% (PROJECT_DIR),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                               'coffeehouse.stores.processors.onsale',
                               'django.template.context_processors.debug',
                               'django.template.context_processors.request',
                               'django.contrib.auth.context_processors.auth',
                               'django.contrib.messages.context_processors.messages',
                               'django.template.context_processors.i18n', 
                               'django.template.context_processors.media', 
                               'django.template.context_processors.static', 
                               'django.template.context_processors.tz',
            ],
        },
    },
]

WSGI_APPLICATION = 'coffeehouse.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'coffehouse',
        'USER': os.getenv('POSTGRES_USR'), 
        'PASSWORD': os.getenv('POSTGRES_PASSWD'), 
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
INTERNAL_IPS = ('127.0.0.1')
STATIC_ROOT = '%s/coffeestatic/'% (BASE_DIR)
STATICFILES_DIRS = ('%s/website-static-default/'% (BASE_DIR),
                    ('bootstrap','%s/bootstrap-3.1.1-dist/'% (BASE_DIR)),
                    ('jquery','%s/jquery-1-11-1-dist/'% (BASE_DIR)),
                    ('jquery-ui','%s/jquery-ui-1.10.4/'% (BASE_DIR)),)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
        'coffeehouse': {
            'handlers': ['console'],
            'level': 'INFO',            
        },        
    }
}
