from django.core.management.base import BaseCommand
from django_celus_registry.tasks import update_registry_models


class Command(BaseCommand):
    help = "Dowload data containing counter registry info"  # noqa

    def handle(self, *args, **options):
        update_registry_models()
