Requirements
============

Django
------
Modern Django versions are supported. Currently this list includes Django 2.*, and 3.2

Python
------
The following Python versions are supported: 3.5, 3.6, 3.7 and 3.8 with a
limit to what Django itself supports. As support for older Django versions is
dropped, the minimum version might be raised. See also `What Python version can
I use with Django?`_.

PyOTP
----------
This project is used for generating one-time passwords. PyOTP_ is a
Python library for generating and verifying one-time passwords. It
can be used to implement two-factor (2FA) or multi-factor (MFA)
authentication methods in web applications and in other systems that
require users to log in.

QRCode
----------------
A Quick Response code (QRCode_) is a two-dimensional pictographic code used
for its fast readability and comparatively large storage capacity.
The code consists of black modules arranged in a square pattern on
a white background. The information encoded can be made up of any
kind of data (e.g., binary, alphanumeric, or Kanji symbols)

Pillow
-----------
PIL_ is the Python Imaging Library adds image processing capabilities
to your Python interpreter. This library provides extensive file
format support, an efficient internal representation, and fairly
powerful image processing capabilities.

.. _PyOTP: https://pypi.org/project/pyotp/
.. _QRCode: https://pypi.org/project/qrcode/
.. _PIL: https://pypi.org/project/Pillow/
.. _What Python version can I use with Django?:
   https://docs.djangoproject.com/en/stable/faq/install/#what-python-version-can-i-use-with-django
.. _django-otp: https://pypi.python.org/pypi/django-otp
.. _Supported versions:
   https://docs.djangoproject.com/en/stable/internals/release-process/#supported-versions