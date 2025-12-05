from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Tag(models.Model):
    """
    Stores a single tag with a unique slug.
    Each tag can be linked to many books.
    """
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
    )
    slug = models.SlugField(max_length=200, blank=True, unique=True)

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
        ("self_development", "Self Development"),
        ("mixed", "Mixed theme"),
    ]
    name = models.CharField(max_length=100, unique=True, blank=False)
    excerpt = models.TextField(blank=True)
    theme = models.CharField(
        max_length=50, choices=THEME_CHOICES, default="mixed")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="collections", null=True
    )
    slug = models.SlugField(max_length=200, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
    title = models.CharField(max_length=200, unique=True, blank=False)
    author = models.CharField(max_length=100, blank=False)
    body = models.TextField()
    finished = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, related_name="books")

    def __str__(self):
        return self.title
