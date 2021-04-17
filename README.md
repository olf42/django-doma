# doma

**doma** is a simple document managment app for django.
It provides the necessary models and view and is ready to be included into your project.

Detailed documentation is in the "docs" directory.

## Installation

Install `django-doma` using pip:

```zsh
$ pip install django-doma
```

## Quick start

1. Add "doma" to your INSTALLED_APPS setting like this::

```python
INSTALLED_APPS = [
    ...
    "doma",
]
```

2. Include the polls URLconf in your project urls.py like this::

    path('doma/', include('doma.urls')),

3. Run ``python manage.py migrate`` to create the doma models.

4. Visit http://127.0.0.1:8000/doma/ to start accounting.
