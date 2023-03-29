from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Blog
from .serializer import BlogSerializer

class LatestBlogsList(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()[0:4]
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

class BlogDetail(APIView):
    def get_object(self, category_slug, blog_slug):
        try:
            return Blog.objects.filter(category__slug=category_slug).get(slug=blog_slug)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, category_slug,blog_slug, format=None):
        blog = self.get_object(category_slug, blog_slug)
        serializer  = BlogSerializer(blog)
        return Response(serializer.data)
# Create your views here.
