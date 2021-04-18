from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _
from io import BytesIO
from pdf2image import convert_from_bytes
from uuid import uuid4

from doma.settings import DOCUMENTS_DIR, PREVIEW_DIR, RENDER_PREVIEW


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


class DocumentManager(models.Manager):
    def replace(self, document, file):
        """
        Even though django recommends to just set the pk to None to duplicate
        an object, we cannot do this here due to the various hooks implemented
        in the init and save methods of Document.
        """
        new_document = self.create(
            name=document.name,
            type=document.type,
            preview=document.preview,
            content=document.content,
            replaces=document,
            file=file,
        )
        return new_document


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
    preview = models.ImageField(upload_to=PREVIEW_DIR, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    replaces = models.OneToOneField(
        "Document",
        on_delete=models.PROTECT,
        related_name="replaced_by",
        null=True,
        blank=True,
    )
    file = models.FileField(upload_to=DOCUMENTS_DIR, blank=True)

    objects = DocumentManager()

    __file = None

    class Meta:
        ordering = ["-created_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__file = self.file

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def save(self, *args, **kwargs):
        if self.pk and self.file != self.__file:
            raise ValidationError(_("Files are not editable."))
        if not self.preview and RENDER_PREVIEW:
            preview = BytesIO()
            convert_from_bytes(self.file.read())[0].save(preview, "JPEG")
            self.preview = SimpleUploadedFile("preview.jpg", preview.read())
        super().save(*args, **kwargs)
