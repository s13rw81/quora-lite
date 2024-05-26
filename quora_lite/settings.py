from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
ENV = os.getenv('ENVIRONMENT', 'DEV')
# ["localhost", "0.0.0.0", "quora-lite.eu-gb.mybluemix.net", "127.0.0.1"]
ALLOWED_HOSTS = [] if ENV == 'DEV' else ["s13rw81.pythonanywhere.com", "0.0.0.0"]
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
CSRF_COOKIE_SECURE = False if ENV == 'DEV' else True
DEBUG = True if ENV == 'DEV' else False
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
LANGUAGE_CODE = "en-in"
LOGIN_REDIRECT_URL = "home"
LOGIN_URL = "login"
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
ROOT_URLCONF = "quora_lite.urls"
SECRET_KEY = os.environ.get("SECRET_KEY", "TABLE")
SECURE_SSL_REDIRECT = False if ENV == 'DEV' else True
SESSION_COOKIE_SECURE = False if ENV == 'DEV' else True
STATICFILES_DIRS = []
STATIC_URL = "/static/"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = "quora_lite.wsgi.application"

INSTALLED_APPS = [
    # user apps
    "blog.apps.BlogConfig",
    "home.apps.HomeConfig",
    "user.apps.UserConfig",
    # default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
]
