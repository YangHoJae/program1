from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(requset, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == requset.user:
            return HttpResponseForbidden()
        return func(requset, *args, **kwargs)
    return decorated