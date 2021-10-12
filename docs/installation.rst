Installation
============

* Download and install last version of Django Admin Two-Factor Authentication:

    .. code-block:: console

        $ pip install django-admin-two-factor

* Add ``admin_two_factor`` application to the ``INSTALLED_APPS`` setting of your Django project ``settings.py`` file (note it should be before ``django.contrib.admin``):

    .. code-block:: python

        INSTALLED_APPS = (
            'admin_two_factor.apps.TwoStepVerificationConfig',
            'django.contrib.admin',
            # ...
        )

* Migrate ``admin_two_factor``:

    .. code-block:: console

        $ python manage.py migrate admin_two_factor
        # or
        $ python manage.py syncdb

.. _PyPI: https://pypi.org/project/django-admin-two-factor/
