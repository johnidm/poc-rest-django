from rest_framework import serializers
from quickstart.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'title', 'slug', 'content', 'posted_on', 'updated_on')
