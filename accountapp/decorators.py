
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def acc_ownership_required(func):
    def decorated(request, *args, **kwargs):
        #본인인증 확인하는 과정
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated