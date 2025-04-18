from pathlib import Path
import os
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# SECURITY SETTINGS
# ---------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-dev-key")  # change in production
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

# Add your deployed domain to allowed hosts
ALLOWED_HOSTS = ['*']

# ---------------------------
# APPLICATIONS
# ---------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'crispy_forms',
    'crispy_bootstrap5',
    'channels',
    'widget_tweaks',

    # Local
    'myapp.apps.MyappConfig',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ---------------------------
# MIDDLEWARE & URLS
# ---------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'
ASGI_APPLICATION = 'myproject.asgi.application'

# ---------------------------
# CUSTOM USER MODEL
# ---------------------------
AUTH_USER_MODEL = 'myapp.User'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = 'urls'

# ---------------------------
# TEMPLATES
# ---------------------------
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

# ---------------------------
# DATABASE (MySQL) -- 🛠 Use real external DB in production
# ---------------------------
# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'ssl': {'ca': os.environ.get('MYSQL_SSL_CA', '')}
        }
    }
}

# Update with DATABASE_URL if present
db_from_env = dj_database_url.config(
    conn_max_age=600,
    conn_health_checks=True,
    default='mysql://root:GO19667543@127.0.0.1:3306/mah'  # Local fallback
)
DATABASES['default'].update(db_from_env)

# Special handling for SSL
if os.environ.get('MYSQL_SSL_MODE', '') == 'required':
    DATABASES['default']['OPTIONS']['ssl'] = {'ca': os.environ.get('MYSQL_SSL_CA')}


# ---------------------------
# CHANNELS (Redis) -- 🛠 Use real external Redis host
# ---------------------------
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(os.getenv("REDIS_HOST", "redis.example.com"), 6379)],  # ❗️Update this!
        },
    },
}

# ---------------------------
# PASSWORD VALIDATION
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------
# LOCALIZATION
# ---------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------------
# STATIC & MEDIA FILES
# ---------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "myapp", "static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ---------------------------
# CACHING (Dummy cache – fine for dev)
# ---------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# ---------------------------
# SECURITY HEADERS (optional prod settings)
# ---------------------------
SECURE_SSL_REDIRECT = os.getenv("DJANGO_SSL_REDIRECT", "False") == "True"
SECURE_HSTS_SECONDS = int(os.getenv("DJANGO_HSTS_SECONDS", 0))

# ---------------------------
# MESSAGES
# ---------------------------
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# ---------------------------
# PRIMARY KEY FIELD
# ---------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
