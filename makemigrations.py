#!/usr/bin/env python

import sys
from pathlib import Path

import django
from django.conf import settings
from django.core.management import call_command

BASE_DIR = Path(__file__).parent
sys.path.insert(0, str(BASE_DIR))


settings.configure(
    BASE_DIR=BASE_DIR,
    DEBUG=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    },
    INSTALLED_APPS=("django_celus_registry",),
    TIME_ZONE="UTC",
    USE_TZ=True,
    USE_I18N=True,
)
django.setup()


call_command("makemigrations", "celus_registry", *sys.argv[1:])

Path("db.sqlite3").unlink()
