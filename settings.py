import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'ii3ojilqw2q-m@%fnfgjx2jyq8!8#ig3q=a$nehdns#b#02n(a'

INSTALLED_APPS = [
    # 'api.apps.ApiConfig',
    'api'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

ALLOWED_HOSTS = []
