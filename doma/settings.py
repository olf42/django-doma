from datetime import timedelta
from django.conf import settings

DOCUMENTS_DIR = getattr(settings, "DOMA_DOCUMENTS_DIR", "documents/")

PROTECT_AFTER = getattr(settings, "DOMA_PROTECT_AFTER", timedelta(days=1))

RENDER_PREVIEW = getattr(settings, "DOMA_RENDER_PREVIEW", True)
