from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI
from blog.api import router as blog_router


"""
With that, Django Ninja will automatically create the following endpoints:

1. /blog/articles/create/ creates a new article
2. /blog/articles/<ARTICLE_ID>/ fetches a single article
3. /blog/articles/ lists all articles

http://127.0.0.1:8000/api/docs
"""

api = NinjaAPI()
api.add_router("/blog/", blog_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
