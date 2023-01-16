from django.http import HttpResponseForbidden
from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(requset, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == requset.user:
            return HttpResponseForbidden()
        return func(requset, *args, **kwargs)

    return decorated
