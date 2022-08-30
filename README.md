# Django Admin Two-Factor Authentication

**Django Admin Two-Factor Authentication**, allows you to login django admin with google authenticator.

<br>

## Why Django Admin Two-Factor Authentication?

- Using google authenticator to login your Django admin.
- Used jquery confirm dialog to get code.
- Simple interface
- Easy integration

<br />

![Django Admin Two-Factor Auth](https://raw.githubusercontent.com/imankarimi/django-admin-two-factor-auth/main/screenshoots/django_admin_two_factor_auth_5.png)

<br />

## How to use it

* Download and install last version of **Django Admin Two-Factor Authentication**:

```bash
$ pip install django-admin-two-factor
# or
$ easy_install django-admin-two-factor
```

* Add 'admin_two_factor' application to the INSTALLED_APPS setting of your Django project `settings.py` file (note it should be before 'django.contrib.admin'):

```python
INSTALLED_APPS = (
'admin_two_factor.apps.TwoStepVerificationConfig',
'django.contrib.admin',
# ...
)
```

* Migrate `admin_two_factor`:

```bash
$ python manage.py migrate admin_two_factor
$ # or
$ python manage.py syncdb
```

* Add `‍‍‍‍ADMIN_TWO_FACTOR_NAME` in your `settings.py`. This value will be displayed in [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en).

```python
ADMIN_TWO_FACTOR_NAME = 'PROJECT_NAME'
```

* Include the **Admin Two Factor** URL config in `PROJECT_CORE/urls.py`:

```python
# Django version >= 2
urlpatterns = [
path('admin/', admin.site.urls),
path('two_factor/', include(('admin_two_factor.urls', 'admin_two_factor'), namespace='two_factor')),
# ...
]

# Django version = 1
# urlpatterns = [
# url(r'^admin/', include(admin.site.urls)),
# url(r'^two_factor/', include(('admin_two_factor.urls', 'admin_two_factor'), namespace='two_factor')),
```

* Collect static if you are in production environment:

```bash
$ python manage.py collectstatic
```

* Clear your browser cache

<br />

## Start the app

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

* Access the `admin` section in the browser: `http://127.0.0.1:8000/`

<br />

## ScreenShoots

<br />

* **User List:** the users who have enabled two-factor auth

![Django Admin Two-Factor Auth: User List](https://raw.githubusercontent.com/imankarimi/django-admin-two-factor-auth/main/screenshoots/django_admin_two_factor_auth_4.png)

<br />
  
* **Add New User:**

![Django Admin Two-Factor Auth: Add New User](https://raw.githubusercontent.com/imankarimi/django-admin-two-factor-auth/main/screenshoots/django_admin_two_factor_auth_2.png)

<br />

* **Scan QRCode and enter the valid code:**

![Django Admin Two-Factor Auth: Scan QRCode](https://raw.githubusercontent.com/imankarimi/django-admin-two-factor-auth/main/screenshoots/django_admin_two_factor_auth_3.png)

<br />

* **Logout and login again with [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en):**

![Django Admin Two-Factor Auth: Login with Code](https://raw.githubusercontent.com/imankarimi/django-admin-two-factor-auth/main/screenshoots/django_admin_two_factor_auth_5.png)

