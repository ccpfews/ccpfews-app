from core.project.settings import ADMIN_PATH

# Allowed Host
ALLOWED_HOSTS = ['ccpfews.uj.ac.za']

# Admin path
ADMIN_PATH = ADMIN_PATH

# Application definition
INSTALLED_APPS = [
    # third party apps by position
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'unfold.contrib.import_export',
    'unfold.contrib.simple_history',

    # core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    # third party apps
    'defender',
    'corsheaders',
    'django_recaptcha',
    'bx_django_utils',
    'import_export',
    'maintenance_mode',
    # app
    'core.blog.apps.BlogConfig',
    'core.contacts.apps.ContactsConfig',
    'core.events.apps.EventsConfig',
    'core.profiles.apps.ProfilesConfig',
    'core.research.apps.ResearchConfig',
    # third party apps by position
    'django_prose_editor',
    'simple_history',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Corsheaders
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Auto logout
    'django_auto_logout.middleware.auto_logout',
    # CSP
    'csp.middleware.CSPMiddleware',
    # Custom csp
    'core.project.settings.middleware.custom_csp.CustomCSPMiddleware',
    # Remote Address Middleware, useful for security
    'core.project.settings.middleware.remoteAddr.RemoteAddrMiddleware',
    # Current request Middleware
    'core.project.settings.middleware.current_request.RequestMiddleware',
    # Simple history middleware
    'simple_history.middleware.HistoryRequestMiddleware',
    # Maintenance mood
    'maintenance_mode.middleware.MaintenanceModeMiddleware',
    # Defender
    'defender.middleware.FailedLoginMiddleware',
]

ROOT_URLCONF = 'core.project.urls'

WSGI_APPLICATION = 'core.project.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_TZ = True

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth Backend
AUTHENTICATION_BACKENDS = [
    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

# Site settings
SITE_ID = 1

# Login
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'account_login'
# LOGOUT_REDIRECT_URL = 'home'
