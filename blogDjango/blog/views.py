from django.http import Http404
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import Blog, Category
from .serializer import BlogSerializer, CategorySerializer


class LatestBlogsList(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()[0:4]
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer= BlogSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetail(APIView):
    def get_object(self, category_slug, blog_slug):
        try:
            return Blog.objects.filter(category__slug=category_slug).get(slug=blog_slug)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, blog_slug, format=None):
        blog = self.get_object(category_slug, blog_slug)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
        query = request.data.get('query', '')

        if query:
            blogs = Blog.objects.filter(Q(name__icontains=query) | Q(content__icontains=query))
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data)

        else:
            return Response({"blogs": []})
# Create your views here.
