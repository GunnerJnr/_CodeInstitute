"""
Staging.py:
"""
from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# disqus shortname
DISQUS_WEBSITE_SHORTNAME = 'gunner'

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_EDwXAGGLO8YWJr05PUpRWFsd')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_DKsnvqPsLCUlxdYDw2hG1FtF')


# Paypal environment variables
PAYPAL_NOTIFY_URL = 'we-are-social-project-staging.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'gunnerjnr-business@live.co.uk'

SITE_URL = 'we-are-social-project-staging.herokuapp.com'
ALLOWED_HOSTS.append('we-are-social-project-staging.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
