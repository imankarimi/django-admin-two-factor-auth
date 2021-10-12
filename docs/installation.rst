Installation
============

* Download and install last version of Django Admin Two-Factor Authentication:

.. code-block:: console

    $ pip install django-admin-two-factor

Setup
-------

* Add ``admin_two_factor`` application to the ``INSTALLED_APPS`` setting of your Django project ``settings.py`` file (note it should be before ``django.contrib.admin``):

.. code-block:: python

    INSTALLED_APPS = (
        'admin_two_factor.apps.TwoStepVerificationConfig',
        'django.contrib.admin',
        ...
    )

* Migrate ``admin_two_factor``:

.. code-block:: console

    $ python manage.py migrate admin_two_factor
    # or
    $ python manage.py syncdb

* Add ``‍‍‍‍ADMIN_TWO_FACTOR_NAME`` in your ``settings.py``. This value will be displayed in `Google Authenticator`_.

.. code-block:: python

    ADMIN_TWO_FACTOR_NAME = 'PROJECT_NAME'


* Include the Admin Two Factor URL config in ``PROJECT_CORE/urls.py``:

.. code-block:: python

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('two_factor/', include(('admin_two_factor.urls', 'admin_two_factor'), namespace='two_factor')),
        ...
    ]


* Collect static if you are in production environment:

.. code-block:: console

    $ python manage.py collectstatic

* Clear your browser cache


.. _PyPI: https://pypi.org/project/django-admin-two-factor/
.. _Google Authenticator: https://support.google.com/accounts/answer/1066447?hl=en
