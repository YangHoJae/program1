
from django.http import HttpResponseForbidden
from profileapp.models import Profile

def profile_ownership_required(func):
    def decorated(requset, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == requset.user:
            return HttpResponseForbidden()
        return func(requset, *args, **kwargs)
    return decorated