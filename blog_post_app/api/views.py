from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import BlogSerializer, AddBlogPostSerializer
from post.models import Post

# for getting list of all blog posts
class BlogView(APIView):

    def get(self,request):
        blog_data = Post.objects.all();
        serializer = BlogSerializer(blog_data, many=True)
        return Response(serializer.data, status=200)

# for getting list of autheticated user's blog posts
class UsersBlogView(APIView):

    def get(self,request):
        try:
            user = Token.objects.get(key=self.request.headers.get('token')).user
            blog_data = Post.objects.filter(post_author = user)
            serializer = BlogSerializer(blog_data, many=True)
            return Response(serializer.data, status=200)
        except Token.DoesNotExist:
            return Response({"message": "Authectication Failed"}, status=406)

# for creating new post
class AddBlogPostView(APIView):

    def post(self,request):
        try:
            user = Token.objects.get(key=self.request.headers.get('token')).user
            serializer = AddBlogPostSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(post_author = user)
            return Response({"message": "Post successfully created"}, status=201)
        except Token.DoesNotExist:
            return Response({"message": "Authectication Failed"}, status=406)
