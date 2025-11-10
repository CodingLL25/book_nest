from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Collection


# Create your views here.
class CollectionList(generic.ListView):
    queryset = Collection.objects.all().order_by("id")

    template_name = "library/index.html"
    paginate_by = 6


def collection_detail(request, slug):
    """
    Display collection.Book`.

    **Context**

    ``post``
        An instance of :model:`collection.Book`.

    """

    queryset = Collection.objects.all().order_by("id")
    collection = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "library/collection_detail.html",
        {"collection": collection},
    )
