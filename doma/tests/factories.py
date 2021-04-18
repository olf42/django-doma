import factory
import factory.django
from pathlib import Path

from django.core.files.uploadedfile import SimpleUploadedFile
from doma.models import Document, DocumentType

DOCUMENT_BASE_PATH = Path(__file__).parent
DOCUMENT_PATH = DOCUMENT_BASE_PATH / "document.pdf"
DOCUMENT_2_PATH = DOCUMENT_BASE_PATH / "document_2.pdf"


def get_test_document(document_path=DOCUMENT_PATH, sup=False):
    with open(document_path, "rb") as infile:
        if sup:
            return SimpleUploadedFile(document_path.name, infile.read())
        else:
            return infile.read()


class DocumentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DocumentType

    name = factory.Sequence(lambda n: "Type %03d" % n)


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Document

    name = factory.Sequence(lambda n: "Document %03d" % n)
    type = factory.SubFactory(DocumentTypeFactory)
    file = factory.django.FileField(
        filename=DOCUMENT_PATH.name, data=get_test_document()
    )
