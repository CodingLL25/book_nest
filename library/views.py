from django.shortcuts import render
from django.views import generic
from .models import Collection


# Create your views here.
class CollectionList(generic.ListView):
    queryset = Collection.objects.all()
    template_name = "library/index.html"
    paginate_by = 6
