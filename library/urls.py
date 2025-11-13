from . import views
from .views import add_book_to_collection, delete_collection, edit_book

from django.urls import path, include

urlpatterns = [
    path("", views.CollectionList.as_view(), name="home"),
    path("accounts/", include("allauth.urls")),
    path("create/", views.create_collection, name="create_collection"),
    path(
        "collection/<slug:slug>/add_book/",
        views.add_book_to_collection,
        name="add_book",
    ),
    path(
        "collection/<slug:slug>/delete_collection/",
        views.delete_collection,
        name="delete_collection",
    ),
    path(
        "collection/<slug:slug>/book/<int:book_id>/edit_book/",
        views.edit_book,
        name="edit_book",
    ),
    path("collection/<slug:slug>/", views.collection_detail, name="collection_detail"),
]
