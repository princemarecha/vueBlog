from django.urls import path, include, re_path
from .views import BlogViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'getBlogs', BlogViewset)

from .views import LatestBlogsList, BlogDetail, CategoryDetail,search

urlpatterns = [
    path('latest-blog/', LatestBlogsList.as_view()),
    path('blogs/search', search),
    path('blogs/<slug:category_slug>/<slug:blog_slug>/', BlogDetail.as_view()),
    path('blogs/<slug:category_slug>/', CategoryDetail.as_view()),
    re_path(r'^',include(router.urls))
]
