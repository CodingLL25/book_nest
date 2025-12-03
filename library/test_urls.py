from django.test import TestCase
from django.urls import reverse, resolve
from library.views import (
    collection_detail,
    edit_collection,
    delete_collection,
    add_book,
    edit_book,
    delete_book,
)


class TestUrls(TestCase):
    """
    Tests to ensure URLs resolve to the correct views.
    """
    def test_collection_detail_url_resolves(self):
        url = reverse("collection_detail", args=["collection-detail-slug"])
        self.assertEqual(resolve(url).func, collection_detail)

    def test_edit_collection_url_resolves(self):
        url = reverse("edit_collection", args=["edit-collection-slug"])
        self.assertEqual(resolve(url).func, edit_collection)

    def test_delete_collection_url_resolves(self):
        url = reverse("delete_collection", args=["delete-collection-slug"])
        self.assertEqual(resolve(url).func, delete_collection)

    def test_add_book_url_resolves(self):
        url = reverse("add_book", args=["add-book-slug"])
        self.assertEqual(resolve(url).func, add_book)

    def test_edit_book_url_resolves(self):
        url = reverse("edit_book", args=["edit-book-slug", 1])
        self.assertEqual(resolve(url).func, edit_book)

    def test_delete_book_url_resolves(self):
        url = reverse("delete_book", args=["delete-book-slug", 1])
        self.assertEqual(resolve(url).func, delete_book)
