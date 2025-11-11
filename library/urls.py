from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.CollectionList.as_view(), name="home"),
    path("accounts/", include("allauth.urls")),
    path("create/", views.create_collection, name="create_collection"),
    path("<slug:slug>/", views.collection_detail, name="collection_detail"),
]
