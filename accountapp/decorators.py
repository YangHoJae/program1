from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(requset, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == requset.user:
            return HttpResponseForbidden()
        return func(requset, *args, **kwargs)
    return decorated