from django.shortcuts import render
from django.views import generic
from .models import Collection


# Create your views here.
class CollectionList(generic.ListView):
    model = Collection
