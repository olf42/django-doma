from django.db.models import ProtectedError
from django.utils import timezone
from django.utils.translation import gettext as _

from doma.settings import PROTECT_AFTER


def protect_documents(sender, instance, **kwargs):
    """
    This signals prevents documents older that PROTECT_AFTER (default: 1 day) from deletion.
    """
    if timezone.now() - instance.created_at > PROTECT_AFTER:
        raise ProtectedError(instance, _("This document cannot be deleted."))
