from django.apps import AppConfig
from django.db.models.signals import pre_delete
from doma.signals import protect_documents


class DomaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "doma"

    def ready(self):
        pre_delete.connect(
            protect_documents, sender="doma.Document", dispatch_uid="delete_document"
        )
