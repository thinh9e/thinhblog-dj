from django.urls.conf import path

from blogs.views import IndexView

app_name = "blogs"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
