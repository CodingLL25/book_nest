from django.test import TestCase
from library.forms import CollectionForm, BookForm
from django.contrib.auth.models import User
from library.models import Collection, Tag


# Automatic testing
class TestCollectionForm(TestCase):
    """
    Automatic testing for collection from to check valid
    and invalid input data.
    """
    def test_form_is_valid(self):
        user = User.objects.create(username="tester")
        data = {
            "name": "My New Collection - testing",
            "theme": "romance",
            "user": user.id,
        }
        collection_form = CollectionForm(data=data)
        self.assertTrue(collection_form.is_valid(), msg=collection_form.errors)

    def test_form_is_invalid(self):
        data = {"name": ""}
        collection_form = CollectionForm(data=data)
        self.assertFalse(collection_form.is_valid(), msg="Form is valid")


class TestBookForm(TestCase):
    """
    Unit tests for the BookForm to verify validation and saving
    of Book instances with tags.
    """
    def setUp(self):
        """
        Create a user and a collection for the book.
        Add tags.
        """
        self.user = User.objects.create(username="tester")
        self.collection = Collection.objects.create(
            name="Test Collection",
            theme="romance",
            user=self.user,
        )
        self.tag1 = Tag.objects.create(name="Feel Good")
        self.tag2 = Tag.objects.create(name="Funny")

    def test_form_is_valid_with_required_fields(self):
        """
        Test for form when all fields are valid.
        """
        data = {
            "title": "My Book",
            "author": "Author Name",
            "body": "Book content",
            "finished": True,
            "tag": [self.tag1.id, self.tag2.id],
        }
        form = BookForm(data=data)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_form_is_invalid_without_title(self):
        """
        Test for form when the title is missing.
        """
        data = {
            "title": "",
            "author": "Author Name",
            "body": "Some content",
            "finished": False,
        }
        form = BookForm(data=data)
        self.assertFalse(
            form.is_valid(), msg="Form should be invalid without a title")

    def test_form_saves_tags_correctly(self):
        """
        Test tags are saved correctly in the form.
        """
        data = {
            "title": "Tagged Book",
            "author": "Author Name",
            "body": "Some content",
            "finished": True,
            "tag": [self.tag1.id, self.tag2.id],
        }
        form = BookForm(data=data)
        self.assertTrue(form.is_valid(), msg=form.errors)
        book = form.save(commit=False)
        book.collection = self.collection
        book.save()
        form.save_m2m()

        self.assertEqual(book.tag.count(), 2)
        self.assertIn(self.tag1, book.tag.all())
        self.assertIn(self.tag2, book.tag.all())
