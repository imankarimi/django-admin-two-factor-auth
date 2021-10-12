from django.contrib.auth import logout

from admin_two_factor.utils import is_expired


def verification(request):
    user = request.user
    can_redirect = False
    if user.is_authenticated and user.is_staff and hasattr(user, 'two_step') and user.two_step.is_active:
        key = 'two_step_%s' % user.id
        user_session = request.session[key] if key in request.session else None
        if not user_session or is_expired(user_session['expire']):
            if user.id:
                logout(request)
                can_redirect = True
    return {'can_redirect': can_redirect}
