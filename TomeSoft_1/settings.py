"""
Django settings for TomeSoft_1 project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
# import firebase_admin #Kevin
# from firebase_admin import credentials #Kevin

# cred = credentials.Certificate("to-me-292901-firebase-adminsdk-jpsas-680a318480.json") #Kevin
# firebase_admin.initialize_app(cred) #Kevin

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i@!=q4ky)pxe0sg&uz%qk&u!2rf2hga6qwh6^3!iopf4nldezq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['tomesoft1.pythonanywhere.com', '127.0.0.1', 'http://localhost:3000/','ccapi-stg.paymentez.com','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_inlinecss',
    'rest_auth',
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'rest_framework',
    'rest_framework.authtoken',
    'fcm_django',
    'api',
]

INSTALLED_APPS += ('naomi',)


REST_FRAMEWORK ={
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication',
        ],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3
    }

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

FCM_DJANGO_SETTINGS = {
         # default: _('FCM Django')
        "APP_VERBOSE_NAME": "ToMe",
         # Your firebase API KEY
        "FCM_SERVER_KEY": "AAAANlvtPYk:APA91bHePBAcH81qKtDdJDaajXqbq6bQ2nsnalFr06fuLe9X7s9v3QMy1JEm7bEUChMS0ADF54Z8wH3drHLe6jbDNbAV9jVnqSDCHL41e50HhROqL-pWL2VztQ08TRpw6oaFBwxnbMsS",
         # true if you want to have only one active device per registered user at a time
         # default: False
        "ONE_DEVICE_PER_USER": True,
         # devices to which notifications cannot be sent,
         # are deleted upon receiving error response from FCM
         # default: False
        "DELETE_INACTIVE_DEVICES": False,
}

MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'TomeSoft_1.urls'
CORS_ORIGIN_ALLOW_ALL = True



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



WSGI_APPLICATION = 'TomeSoft_1.wsgi.application'

AUTHENTICATION_BACKENDS = {
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'

    }


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tomesoft1$tome-db',
        'USER': 'tomesoft1',
        'PASSWORD': 'Software1',
        'HOST': 'tomesoft1.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'TEST': {
            'NAME': '<tomesoft1>$test_<tomesoft1$Tome-soft-db-1>',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email','public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'kr_KR',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}
        }


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT= 587
EMAIL_HOST_USER= 'vivefacil2022@gmail.com'
EMAIL_HOST_PASSWORD= 'eggtkwfyeqmvjtre'
# EMAIL_HOST_PASSWORD= 'Academico96.'
# EMAIL_USE_SSL=False
# EMAIL_HOST_USER= 'tometestemail@gmail.com'
# EMAIL_HOST_USER= 'vivefacil2020@gmail.com'

# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # Ruta absoluta donde se recopilarán los archivos estáticos
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
ACCOUNT_EMAIL_VERIFICATION='none'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_AUTHENTICATION_METHOD='username'

SERVER_APP_CODE= 'INNOVA-EC-SERVER'
SERVER_APP_KEY= 'Y5FnbpWYtULtj1Muvw3cl8LJ7FVQfM'

CLIENT_APP_CODE=  'INNOVA-EC-CLIENT'
CLIENT_APP_KEY= 'ZjgaQCbgAzNF7k8Fb1Qf4yYLHUsePk'

PAYMENTEZ_HOST= 'https://ccapi-stg.paymentez.com/'

if DEBUG and False:  #si estas en modo desarrollo elimina la condicion 'and False'
    EMAIL_BACKEND = "naomi.mail.backends.naomi.NaomiBackend"
    EMAIL_FILE_PATH = "/home/tomesoft1/TomeSoft_1/tmp"


