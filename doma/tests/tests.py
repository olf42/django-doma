from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.test import TestCase
from freezegun import freeze_time

from doma.tests.factories import DocumentFactory, DocumentTypeFactory, get_test_document


class DomaTestCase(TestCase):
    def setUp(self):
        self.t = DocumentTypeFactory()

    def test_document_delete_protect(self):
        """Tests if the PROTECT_AFTER switch works correctly."""
        with freeze_time("2021-01-01"):
            t_old = DocumentFactory()
        self.assertRaises(ProtectedError, t_old.delete)

    def test_preview_image(self):
        """Test if a preview image is set for the document."""
        d = DocumentFactory()
        self.assertIsNotNone(d.preview)

    def test_document_delete(self):
        """Tests if the PROTECT_AFTER switch works correctly."""
        t_new = DocumentFactory()
        t_new.delete()

    def test_file_change(self):
        d = DocumentFactory()
        d.file = get_test_document(sup=True)
        self.assertRaises(ValidationError, d.save)
