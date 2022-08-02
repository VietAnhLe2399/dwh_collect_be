from .base import *

ENV_FILE = 'settings/.env.prod'
env_config = Config(RepositoryEnv(os.path.join(BASE_DIR, ENV_FILE)))

DEBUG = env_config.get('DEBUG', False)

SECRET_KEY = os.environ["SECRET_KEY"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env_config.get('DATABASE_ENGINE'),
        'NAME': env_config('DATABASE_NAME'),
        'USER': env_config('DATABASE_USER'),
        'PASSWORD': env_config('DATABASE_PASSWORD'),
        'HOST': env_config('DATABASE_HOST'),
        'PORT': env_config('DATABASE_PORT'),
    }
}
