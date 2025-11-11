from . import views
from .views import delete_collection, add_book_to_collection

from django.urls import path, include

urlpatterns = [
    path("", views.CollectionList.as_view(), name="home"),
    path("accounts/", include("allauth.urls")),
    path("create/", views.create_collection, name="create_collection"),
    path(
        "collection/<int:collection_id>/add-book/",
        add_book_to_collection,
        name="add_book",
    ),
    path("collection/<slug:slug>/delete/", delete_collection, name="collection_delete"),
    path("<slug:slug>/", views.collection_detail, name="collection_detail"),
]
