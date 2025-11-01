from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Tag(models.Model):
    """Tag model"""

    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
    )

    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Collection(models.Model):
    """
    Stores a single collection related to :model:`auth.User`.
    """

    THEME_CHOICES = [
        ("romance", "Romance"),
        ("fantasy", "Fantasy"),
        ("mystery", "Mystery"),
        ("historical", "Historical"),
        ("thriller", "Thriller"),
        ("science_fiction", "Science Fiction"),
        ("nonfiction", "Nonfiction"),
        ("young_adult", "Young Adult"),
        ("literary", "Literary Fiction"),
        ("horror", "Horror"),
        ("mixed", "Mixed theme"),
    ]

    name = models.CharField(max_length=100, unique=True)
    edited_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    theme = models.CharField(max_length=50, choices=THEME_CHOICES, default="NA")

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
