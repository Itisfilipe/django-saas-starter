from .django import env

CACHES = {'default': env.cache('REDIS_CACHE_URL')}
