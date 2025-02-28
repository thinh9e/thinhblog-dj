from django.urls.conf import path

from blogs import views

urlpatterns = [
    path("", views.index, name="index"),
]
