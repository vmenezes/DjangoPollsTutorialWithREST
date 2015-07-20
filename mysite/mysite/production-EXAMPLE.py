"""
This is a production.py example that have configs for heroku.
The original production.py is not on Github to keep the
SECRET_KEY used on production private.
"""
import dj_database_url

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@123456(4bsf$+w+$^0e_*j#*)_0ekaj2%v3@27f4m8i&rlkjh'

DATABASES = {
    'default': dj_database_url.config()
}