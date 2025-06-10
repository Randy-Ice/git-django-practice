from rest_framework.serializers import ModelSerializer

from blog.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'image', 'author'
        ]
        read_only_fields = ['created_at', 'updated_at', 'author']


class FakeSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'image', 'author'
        ]
        #other notes