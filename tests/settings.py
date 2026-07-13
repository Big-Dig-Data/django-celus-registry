SECRET_KEY = "test"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

INSTALLED_APPS = ["django_celus_registry"]

USE_TZ = True
