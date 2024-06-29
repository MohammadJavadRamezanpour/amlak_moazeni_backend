"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import dj_database_url

from .common import *

SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ["DEBUG"]

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = ALLOWED_HOSTS
CORS_ALLOW_ALL_ORIGINS = DEBUG

DATABASES = {
    'default': dj_database_url.config()
}
