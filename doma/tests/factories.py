import factory
import factory.django

from django.core.files import SimpleUploadedFile
from doma.models import Document, DocumentType


class DocumentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DocumentType

    name = factory.Sequence(lambda n: "Type %03d" % n)


class DocumenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Document

    name = factory.Sequence(lambda n: "Document %03d" % n)
    type = factory.SubFactory(DocumentTypeFactory)
    file = SimpleUploadedFile("document.pdf", b"123")
