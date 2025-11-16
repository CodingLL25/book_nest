from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Collection, Book
from .forms import CollectionForm, BookForm


class AboutPage(TemplateView):
    """
    Class based view to show about page.
    """

    template_name = "library/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["example_collections"] = Collection.objects.filter(
            user__username="Example"
        )
        return context


class CollectionList(LoginRequiredMixin, generic.ListView):
    """
    Class based view to show collections for a logged in user.
    """

    template_name = "library/index.html"
    paginate_by = 3

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user).order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CollectionForm()
        return context


def collection_detail(request, slug):
    """
    Function to show relevant collection details for logged in user
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
    Function to create a new collection for logged in user
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
def edit_collection(request, slug):
    collection = get_object_or_404(Collection, slug=slug)

    if collection.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this collection.")

    if request.method == "POST":
        collection_form = CollectionForm(request.POST, instance=collection)
        if collection_form.is_valid():
            collection = collection_form.save(commit=False)
            collection = collection
            collection.save()
            collection_form.save_m2m()
            messages.success(request, "Collection has been updated!")
            return redirect("/")
    else:
        collection_form = CollectionForm(instance=collection)

    return render(
        request,
        "library/edit_collection.html",
        {
            "collection_form": collection_form,
            "collection": collection,
        },
    )


@login_required
def add_book(request, slug):
    """
    Function to add a book to a collection for logged in user.
    Only allowed to add books to their collections.
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
        "library/add_book.html",
        {
            "form": form,
            "collection": collection,
        },
    )


@login_required
def edit_book(request, slug, book_id):
    collection = get_object_or_404(Collection, slug=slug)
    book = get_object_or_404(Book, pk=book_id)

    if collection.user != request.user:
        return HttpResponseForbidden(
            "You are not allowed to edit books in this collection."
        )

    if request.method == "POST":
        book_form = BookForm(request.POST, instance=book)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.collection = collection
            book.save()
            book_form.save_m2m()
            messages.success(request, "Book has been updated!")
            return redirect("collection_detail", slug=slug)
    else:
        book_form = BookForm(instance=book)

    return render(
        request,
        "library/edit_book.html",
        {
            "book_form": book_form,
            "collection": collection,
            "book": book,
        },
    )


@login_required
def delete_book(request, slug, book_id):
    """
    Function to delete existing books in the collection.
    Only able to delete books in their collection.
    """
    collection = get_object_or_404(Collection, slug=slug)
    book = get_object_or_404(Book, pk=book_id)

    if collection.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this book.")
    if request.method == "POST":
        book.delete()
        return redirect("collection_detail", slug=collection.slug)

    return render(
        request,
        "library/delete_book.html",
        {
            "collection": collection,
            "book": book,
        },
    )


@login_required
def delete_collection(request, slug):
    """
    Function to delete collections.
    Only able to delete their collection.
    """
    collection = get_object_or_404(Collection, slug=slug)

    if collection.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this collection.")
    if request.method == "POST":
        collection.delete()
        return redirect("collections")

    return render(request, "library/delete_collection.html", {"collection": collection})
