from .django import env


DATABASES = {'default': env.db('DATABASE_URL')}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
