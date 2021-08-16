"""
Django settings for pento_arts project.
Generated by 'django-admin startproject' using Django 3.0.2.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path

# プロジェクトのベースフォルダを示す
BASE_DIR = Path(__file__).resolve().parent.parent
REPOSITORY_ROOT = os.path.dirname(BASE_DIR)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

SECRET_KEY = 'v0h+s=#9_a^gxs+7=oto*nv=i+7x0_72___8s)sxlhi#sx1f9*'

#デバッグモードを有効化。エラー発生時にブラウザ上にエラーの詳細情報を表示する。
DEBUG = False

#サーバが受理するサーバアドレスを指定する。この値を正確に記述することは「Hostヘッダインジェクション攻撃」に対して有効
ALLOWED_HOSTS = ["kentaro-test-app.herokuapp.com", "*"]


# Application definition

INSTALLED_APPS = [
    'pento_app.apps.PentoAppConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'bootstrap4',
    'imagekit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


ROOT_URLCONF = 'pento_arts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
WSGI_APPLICATION = 'pento_arts.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_ROOT = BASE_DIR.joinpath('media')
MEDIA_URL = '/media/'


#プロジェクト全体で使用するUserモデル
AUTH_USER_MODEL = 'pento_app.CustomUser'

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = True

LOGIN_REDIRECT_URL = 'pento_app:index'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

DEFAULT_FROM_EMAIL = 'pento-arts@example.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#メールに記載するサイトのURLを設定
FRONTEND_URL = "http://127.0.0.1:8000/"
