from django.conf import settings
from django.db import models
from django.utils.text import slugify
from uuid import uuid4

DOCUMENTS_DIR = getattr(settings, "DOMA_DOCUMENTS_DIR", "documents/")


class CreatedModifiedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class SlugifiedModel(models.Model):
    slug = models.SlugField(editable=False, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class DocumentType(SlugifiedModel):
    name = models.CharField(max_length=255)


class Document(CreatedModifiedModel):
    """
    The default ordering is by created_at (desc), because the contents of a document,
    are given to the renderer upon creation of the instance. After rendering it is
    updated (i.e. modified) but can already be out of date.
    """

    name = models.CharField(max_length=255)
    type = models.ForeignKey(
        "DocumentType", on_delete=models.PROTECT, related_name="documents"
    )
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    preview = models.ImageField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    replaces = models.ForeignKey(
        "Document",
        on_delete=models.PROTECT,
        related_name="replaced_by",
        null=True,
        blank=True,
    )
    file = models.FileField(upload_to=DOCUMENTS_DIR, null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.pk} - {self.name}"
