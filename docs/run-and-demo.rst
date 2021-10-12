Run & Demo
##############

Run
-----

.. code-block:: console

    # Set up the database
    $ python manage.py makemigrations
    $ python manage.py migrate

    # Create the superuser
    $ python manage.py createsuperuser

    # Start the application (development mode)
    $ python manage.py runserver # default port 8000

Access the ``admin`` section in the browser: ``http://127.0.0.1:8000/``

Demo
------

**User List:** the users who have enabled two-factor auth

.. image:: https://raw.githubusercontent.com/imankarimi/django-admin-two-factor-auth/main/screenshoots/django_admin_two_factor_auth_4.png
    :alt: User List

| **Add New User:**

.. image:: https://raw.githubusercontent.com/imankarimi/django-admin-two-factor-auth/main/screenshoots/django_admin_two_factor_auth_2.png
    :alt: Add New User

| **Scan QRCode and enter the valid code:**

.. image:: https://raw.githubusercontent.com/imankarimi/django-admin-two-factor-auth/main/screenshoots/django_admin_two_factor_auth_3.png
    :alt: Scan QRCode and enter the valid code

| **Logout and login again with** `Google Authenticator`_:

.. image:: https://raw.githubusercontent.com/imankarimi/django-admin-two-factor-auth/main/screenshoots/django_admin_two_factor_auth_5.png
    :alt: Logout and login


.. _Google Authenticator: https://support.google.com/accounts/answer/1066447?hl=en

