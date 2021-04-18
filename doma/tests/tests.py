from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import ProtectedError
from django.test import TestCase
from doma.models import Document, DocumentType
from freezegun import freeze_time
from pathlib import Path

DOCUMENT_PATH = Path(__file__).parent / "document.pdf"


def get_test_document(document_path=DOCUMENT_PATH):
    with open(document_path, "rb") as infile:
        return SimpleUploadedFile("document.pdf", infile.read())


class DomaTestCase(TestCase):
    def setUp(self):
        self.t = DocumentType.objects.create(name="Test Document")

    def test_document_create(self):
        """Test if an entry can have both filled debit and credit (shouldn't be possible)."""
        Document.objects.create(
            name="Test document", type=self.t, file=get_test_document()
        )

    def test_document_delete(self):
        with freeze_time("2021-01-01"):
            self.t_old = Document.objects.create(
                name="Old Test Document", type=self.t, file=get_test_document()
            )
        self.assertRaises(ProtectedError, self.t_old.delete)
