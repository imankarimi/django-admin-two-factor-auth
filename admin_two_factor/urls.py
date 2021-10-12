from django.urls import path

from admin_two_factor.views import TwoStepVerification

urlpatterns = [
    path('verification/', TwoStepVerification.as_view(), name='verification'),
]
