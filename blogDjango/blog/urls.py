from django.urls import path, include

from .views import LatestBlogsList, BlogDetail

urlpatterns = [
    path('latest-blog/', LatestBlogsList.as_view()),
    path('blogs/<slug:category_slug>/<slug:blog_slug>/', BlogDetail.as_view())
]
