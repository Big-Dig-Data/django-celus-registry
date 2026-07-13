from unittest.mock import patch

from django.core.management import call_command


def test_download_registry_calls_update_registry_models():
    with patch(
        "django_celus_registry.management.commands.download_registry.update_registry_models"
    ) as mocked:
        call_command("download_registry")

    mocked.assert_called_once()
