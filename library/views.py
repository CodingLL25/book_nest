from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Collection
from .forms import CollectionForm, BookForm


# Create your views here.
class CollectionList(generic.ListView):
    """
    ADD DESCRIPTION WHEN CLEANING UP CODE
    """

    queryset = Collection.objects.all().order_by("id")
    template_name = "library/index.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CollectionForm()
        return context


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


def create_collection(request):
    """
    Function to create a new collection
    """
    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save()
            # Redirect to the new (empty) collection’s page
            return redirect("collection_detail", slug=collection.slug)
    else:
        form = CollectionForm()

    return render(request, "collection_detail.html", {"form": form})


def add_book_to_collection(request, collection_id):
    """
    Function to add a book to a collection
    """
    collection = get_object_or_404(Collection, id=collection_id)

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.collection = collection
            book.save()
            return redirect("collection_detail", slug=collection.slug)
    else:
        form = BookForm()

    return render(
        request,
        "library/add_book.html",
        {
            "form": form,
            "collection": collection,
        },
    )
