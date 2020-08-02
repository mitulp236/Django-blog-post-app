from rest_framework import serializers
from post.models import Post

# blog post serializer
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

# crete blog post serialization
class AddBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_title', 'post_text')
