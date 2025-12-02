from .models import Collection, Book
from django import forms


class CollectionForm(forms.ModelForm):
    """
    A form for creating and updating Collection instances.
    """
    class Meta:
        model = Collection
        fields = (
            "name",
            "excerpt",
            "theme",
        )


class BookForm(forms.ModelForm):
    """
    A form for creating and updating Book instances.
    """
    class Meta:
        model = Book
        fields = ("title", "author", "body", "finished", "tag")
        help_texts = {
            "tag": "CTRL-click to select multiple tags",
        }
