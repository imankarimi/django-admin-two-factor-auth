import django
from admin_two_factor.views import TwoStepVerification

if django.VERSION[0] >= 2:
    from django.urls import path

    urlpatterns = [
        path('verification/', TwoStepVerification.as_view(), name='verification'),
    ]
else:
    from django.conf.urls import url

    urlpatterns = [
        url(r'^verification/', TwoStepVerification.as_view(), name='verification'),
    ]
