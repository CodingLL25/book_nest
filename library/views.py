from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Collection


# Create your views here.
class CollectionList(generic.ListView):
    """
    ADD DESCRIPTION WHEN CLEANING UP CODE
    """

    queryset = Collection.objects.all().order_by("id")

    template_name = "library/index.html"
    paginate_by = 6


def collection_detail(request, slug):
    """
    ADD DESCRIPTION WHEN CLEANING UP CODE
    """
    queryset = Collection.objects.all().order_by("id")
    collection = get_object_or_404(queryset, slug=slug)
    books = collection.books.all()

    return render(
        request,
        "library/collection_detail.html",
        {
            "collection": collection,
            "books": books,
        },
    )
