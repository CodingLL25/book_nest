from . import views
from django.urls import path

urlpatterns = [
    path("", views.CollectionList.as_view(), name="home"),
    path("create/", views.create_collection, name="create_collection"),
    path("<slug:slug>/", views.collection_detail, name="collection_detail"),
]
