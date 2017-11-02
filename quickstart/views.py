
from rest_framework import viewsets
from quickstart.serializers import PostSerializer
from quickstart.models import Post


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
