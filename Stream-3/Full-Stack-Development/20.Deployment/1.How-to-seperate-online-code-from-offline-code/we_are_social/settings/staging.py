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
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<YOUR SECRET KEY HERE>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<YOUR SECRET KEY HERE>')
 
# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://<your ngrok URL>/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = '<your paypal merchant email goes here>'
 
SITE_URL = 'https://your-heroku-app.herokuapp.com'
ALLOWED_HOSTS.append('your-heroku-app.herokuapp.com')
 
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
