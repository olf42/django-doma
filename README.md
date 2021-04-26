# doma

**doma** is a simple document managment app for django.
It provides the necessary models and view and is ready to be included into your project.

Detailed documentation is in the "docs" directory.

![django_doma_logo](assets/django-doma-logo.png?raw=true "django-doma-logo")

## Idea

Many modern (accounting, business) applications work with digital documents. This app aims to provide easy integration of digital documents into your Django application, if you have no central Document Management System like Mayan EDMS.

## Features

_Django-doma_ currently provides some models which are ready to be used in our application

* Document model to store documents
* DocumentType to group/order documents

Documents will become readonly after a while, this helps storing your documents audit-proof.
Once readonly, Documents can not be deleted, but only "replaced", i.e. an updated version is 
linked, but the original is kept in place (as a sort of version control).

## Apps using django-doma

* [django-kesha](https://github.com/olf42/django-kesha) - Accounting App

## Compatibility

Tested with the following versions of Python/Django:

* Django: 2.2, 3.0,, 3.1, 3.2
* Python: 3.7, 3.8, 3.9
* Pypy: Pypy3


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

## License

MIT

## Copyright

2021, Florian Rämisch

## Authors

* Florian Rämisch
