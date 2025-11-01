from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """Tag model"""

    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
    )

    def __str__(self):
        return self.name


class Collection(models.Model):
    """
    Stores a single collection related to :model:`auth.User`.
    """

    name = models.CharField(max_length=100, unique=True)
    edited_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    # featured_image = models.ImageField(upload_to='collection_images/', blank=True, null=True)
    # book_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Stores a single book related to :model:`auth.User`
    and :model:`library.Collection`.
    """

    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name="books"
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    body = models.TextField()
    finished = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
