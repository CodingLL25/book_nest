from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.AboutPage.as_view(), name="home"),
    path("collections/", views.CollectionList.as_view(), name="collections"),
    path("accounts/", include("allauth.urls")),
    path("create/", views.create_collection, name="create_collection"),
    path(
        "collection/<slug:slug>/edit_collection/",
        views.edit_collection,
        name="edit_collection",
    ),
    path(
        "collection/<slug:slug>/add_book/",
        views.add_book,
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
    path(
        "collection/<slug:slug>/book/<int:book_id>/delete_book/",
        views.delete_book,
        name="delete_book",
    ),
    path("collection/<slug:slug>/", views.collection_detail, name="collection_detail"),
]
