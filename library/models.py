from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Collection(models.Model):
    """
    Stores a single collection related to :model:`auth.User`.
    """

    name = models.CharField(max_length=100, unique=True)
    edited_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    # add featured image?
    # add book number?


class Book(models.Model):
    """
    Stores a single book related to :model:`auth.User`
    and :model:`library.Collection`.
    """

    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name="comments"
    )
    title = models.TextField(max_length=200)
    author = models.TextField(max_length=100)
    body = models.TextField(max_length=500)
    finished = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


# Taken directly from e-commerce from Iuliia - E-commerce
class Tag(models.Model):
    """Tag model"""

    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
        verbose_name="Tag name",
        help_text="format: required, max_length=100",
    )

    is_active = models.BooleanField(
        default=False,
    )
