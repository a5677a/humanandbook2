
from django.http import HttpResponseForbidden
from profileapp.models import Profile


def pf_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = Profile.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated