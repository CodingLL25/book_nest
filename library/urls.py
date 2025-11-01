from . import views
from django.urls import path

urlpatterns = [
    path("", views.CollectionList.as_view(), name="home"),
]
