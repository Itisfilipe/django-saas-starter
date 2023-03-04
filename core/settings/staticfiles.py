from .django import root, env

STATIC_URL = env.str('STATIC_URL')
STATIC_ROOT = root("staticfiles/")
STATICFILES_DIRS = [root("assets", "dist")]
MEDIA_URL = env.str('MEDIA_URL')
MEDIA_ROOT = root("mediafiles/")
