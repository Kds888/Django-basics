"""
Django settings for one project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f(qcrgw8zmi4!59hx2xf9$8b(2(uds77h4f2u$c!9i1vd_(!$4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
# custom 404 page will run once we disable the debug mode in django 


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',# used for authentication 
    'django.contrib.contenttypes',# also for authentication
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'one_one.apps.OneOneConfig',#templates and  One_one is the basic explanation of how to send variables to the template and how to render templates.
    # if we include the application we no longer have to tell the django to include the templates in the templates list that is defined below as it has 
    # apps dir as true
    'office.apps.OfficeConfig',
    # connecting the office app
    'cars.apps.CarsConfig',
    # connecting the cars app
    'classroom.apps.ClassroomConfig',
    'library.apps.LibraryConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',# required for authentication
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'one.urls'
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        # the above statement is used to connect the templates project level folder with the base directory
        'APP_DIRS': True,
        # this tells the django to look for templates according to the apps directory where they must be stired in app_name/templates/app_name/ then your .html files
        'OPTIONS': {
            'context_processors': [ # COntext processors can be passed in any templates without any problems.
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'one.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # this is path we can also define this by os.path.join(Base_DIR,'db.sqlite3')
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# static folder should be created like this one_one/static/one_one/ your static files for that platform 
# right now we don't have it for project level implementation

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL='/'# taking the login page to the home page



