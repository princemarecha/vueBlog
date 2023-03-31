from rest_framework import serializers

from .models import Category, Blog


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    class Meta:
        model = Blog
        fields = (
            "id",
            "name",
            "author",
            "get_absolute_url",
            "image",
            "category",
            "slug",
            "content",
            "get_image",
            "get_thumbnail",
            "date_added"
        )


class CategorySerializer(serializers.ModelSerializer):
    blog = BlogSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "blog",
        )
