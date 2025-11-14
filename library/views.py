from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponseRedirect
from .models import Collection, Book
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


@login_required
def create_collection(request):
    """
    Function to create a new collection
    """
    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user
            collection.save()
            return redirect("collection_detail", slug=collection.slug)
    else:
        form = CollectionForm()

    return render(request, "library/create_collection.html", {"form": form})


@login_required
def add_book_to_collection(request, slug):
    """
    Function to add a book to a collection
    """
    collection = get_object_or_404(Collection, slug=slug)

    if collection.user != request.user:
        return HttpResponseForbidden(
            "You are not allowed to add books to this collection."
        )

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
        "library/collection_detail.html",
        {
            "form": form,
            "collection": collection,
        },
    )


@login_required
def edit_book(request, slug, book_id):
    """
    Function to edit existing books in the collection
    """
    if request.method == "POST":
        queryset = Collection.objects.all()
        collection = get_object_or_404(queryset, slug=slug)
        book = get_object_or_404(Book, pk=book_id)
        book_form = BookForm(data=request.POST, instance=book)

        if book_form.is_valid() and collection.user == request.user:
            book = book_form.save(commit=False)
            book.collection = collection
            book.save()
            messages.add_message(request, messages.SUCCESS, "Book has been updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating book!")

    return HttpResponseRedirect(reverse("collection_detail", args=[slug]))


@login_required
def delete_book(request, slug, book_id):
    """
    Function to delete existing books in the collection
    """
    collection = get_object_or_404(Collection, slug=slug)
    book = get_object_or_404(Book, pk=book_id)

    if collection.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this book.")

    if request.method == "POST":
        book.delete()
        return redirect("collection_detail", slug=collection.slug)


@login_required
def delete_collection(request, slug):
    """
    Function to delete collections
    """
    collection = get_object_or_404(Collection, slug=slug)

    if collection.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this collection.")

    if request.method == "POST":
        collection.delete()
        return redirect("/")
