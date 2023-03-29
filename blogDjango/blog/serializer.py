from rest_framework import serializers

from .models import Category, Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "content",
            "get_image",
            "get_thumbnail"
        )