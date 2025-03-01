from django.contrib import admin
from django.urls import include, path

from thinhblog.views import IndexView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", include("blogs.urls")),
    path("", IndexView.as_view(), name="home"),
]
