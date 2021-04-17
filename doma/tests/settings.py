import tempfile

USE_TZ = False
SECRET_KEY = "fake_key_for_testing"
INSTALLED_APPS = [
    "doma",
    "doma.tests",
]
MEDIA_ROOT = tempfile.mkdtemp(prefix="django-doma_test")
DATABASES = dict(
    default=dict(
        ENGINE="django.db.backends.sqlite3",
        NAME=":memory:",
    )
)
