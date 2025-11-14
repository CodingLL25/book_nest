from .models import Collection, Book
from django import forms


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = (
            "name",
            "excerpt",
            "theme",
        )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "body", "finished", "tag")
