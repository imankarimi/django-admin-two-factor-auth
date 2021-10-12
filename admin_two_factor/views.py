from urllib.parse import parse_qsl

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from admin_two_factor.utils import set_expire


class TwoStepVerification(View):
    def post(self, request):
        params = dict(parse_qsl(request.body.decode()))
        username = params.get('username', None)
        password = params.get('password', None)
        if not username or not password:
            return JsonResponse({'is_valid': False, 'message': 'required username/password'})

        user = authenticate(request=request, username=username, password=password)
        if user and user.is_staff:
            if hasattr(user, 'two_step') and user.two_step.is_active:
                return JsonResponse({'is_valid': True, 'message': 'ok'})
        return JsonResponse({'is_valid': False, 'message': 'maybe something wrong'})

    @csrf_exempt
    def put(self, request):
        params = dict(parse_qsl(request.body.decode()))
        code = params.get('code', None)
        username = params.get('username', None)
        password = params.get('password', None)
        if not username or not password:
            return JsonResponse({'is_valid': False, 'message': 'required username/password'})
        if not code:
            return JsonResponse({'is_valid': False, 'message': 'provide a valid code. The code is required.'})

        user = authenticate(request=request, username=username, password=password)
        if user and user.is_staff:
            if hasattr(user, 'two_step') and user.two_step.is_active:
                if user.two_step.is_verify(code):
                    request.session['two_step_%s' % user.id] = {'expire': set_expire().get('time')}
                    return JsonResponse({'is_valid': True, 'message': 'ok'})
                else:
                    return JsonResponse({'is_valid': False, 'message': 'please provide a valid code'})

        return JsonResponse({'is_valid': False, 'message': 'something wrong happened'})

