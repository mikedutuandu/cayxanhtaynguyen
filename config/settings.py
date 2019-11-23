"""
Django settings for ecommerce2 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import datetime
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#root of project

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'csqwlmc8s55o($rt6ozh7u+ui9zb-et00w$d90j8$^!nvj41_r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_HOST = 'smtp.sendgrid.com'
EMAIL_HOST_USER = 'teamcfe' #hello@teamcfe.com
EMAIL_MAIN = 'hello@teamcfe.com'
EMAIL_HOST_PASSWORD = 'codeon2016'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

''' 
If using gmail, you will need to
unlock Captcha to enable Django 
to  send for you:
https://accounts.google.com/displayunlockcaptcha
'''



# Application definition

INSTALLED_APPS = (
    #django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    #third party apps
    'corsheaders',
    'crispy_forms',
    'django_filters',
    'rest_framework',
    'imagekit',
    'el_pagination',
    'debug_toolbar',
    'ckeditor',
    'ckeditor_uploader',
    #django allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    #my apps
    'apps.carts',
    'apps.pages',
    'apps.orders',
    'apps.products',
    'apps.accounts',
    'apps.comments',
    'apps.posts',
)
SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# CORS_ORIGIN_WHITELIST = (
#     'ang.heroku.com'
# )

# CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://)?(\w+\.)?teamcfe\.com$', )
CORS_URLS_REGEX = r'^/api/.*$'



ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cayxanhtaynguyen',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '68.183.230.245',
        'PORT': '3306',
        'OPTIONS': {
           'sql_mode': 'STRICT_TRANS_TABLES',
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "statics"),
    #os.path.join(BASE_DIR, "static_in_env"),
    #'/var/www/static/',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




#Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'




#DJANGO AllAUTH
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


#django allauth
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_ADAPTER = 'apps.accounts.allauth.AccountAdapter'

SOCIALACCOUNT_PROVIDERS = {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
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
        'LOCALE_FUNC':  lambda request: 'en_US',
        'VERIFIED_EMAIL': True,
        'VERSION': 'v2.4'}}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

#debug toolbar
INTERNAL_IPS =['127.0.0.1']

#Braintree Payments Details
BRAINTREE_PUBLIC = "qn3p5n7njksw47r3"
BRAINTREE_PRIVATE = "d14ac944794c0df1c81991ecf49221ff"
BRAINTREE_MERCHANT_ID = "n84nynknvzz3j3sz"
BRAINTREE_ENVIRONEMNT = "Sandbox"

#paging
EL_PAGINATION_PER_PAGE = 20

#django ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        # 'height': 300,
        # 'width': 300,
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
      'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
    ),
      'DEFAULT_PAGINATION_CLASS': 'apps.products.pagination.ProductPagination',
      "SEARCH_PARAM" : "q"
}

JWT_AUTH = {
    "JWT_RESPONSE_PAYLOAD_HANDLER": 
            "apps.accounts.api.jwt.jwt_response_payload_handler",
    "JWT_EXPIRATION_DELTA": datetime.timedelta(seconds=30000),
    "JWT_ALLOW_REFRESH": True, #False
}











