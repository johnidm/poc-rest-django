from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from quickstart.models import Post


class PostResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'title': 'title',
        'author': 'user.username',
        'body': 'content',
        'posted_on': 'posted_on',
    })

    # GET /api/posts/ (but not hooked up yet)
    def list(self):
        return Post.objects.all()

    # GET /api/posts/<pk>/ (but not hooked up yet)
    def detail(self, pk):
        return Post.objects.get(id=pk)