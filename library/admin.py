from django.contrib import admin
from .models import Collection, Book, Tag
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.admin import SimpleListFilter
from django.utils.html import strip_tags


def clean_html(text):
    return strip_tags(text)


class TagFilter(SimpleListFilter):
    """
    Custom list filter for the Django admin interface.
    This filter adds a dropdown in the Book admin that allows
    filtering books by their associated tags.
    """
    title = "Tag"
    parameter_name = "tag"

    def lookups(self, request, model_admin):
        return [(tag.id, tag.name) for tag in Tag.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(tag__id=self.value()).distinct()
        return queryset


@admin.register(Collection)
class Collection(SummernoteModelAdmin):
    """
    Custom Django admin configuration for the Collection model.
    """
    list_display = ("name", "theme", "excerpt_clean")
    search_fields = ["theme", "excerpt"]
    list_filter = (TagFilter, "theme")
    summernote_fields = ("excerpt",)

    @admin.display(description="excerpt")
    def excerpt_clean(self, obj):
        return clean_html(obj.excerpt)


@admin.register(Book)
class Book(SummernoteModelAdmin):
    """
    Custom Django admin configuration for the Book model.
    """
    list_display = ("title", "author", "body_clean")
    search_fields = ["title", "author"]
    list_filter = (TagFilter, "author")
    summernote_fields = ("body",)

    @admin.display(description="body")
    def body_clean(self, obj):
        return clean_html(obj.body)


# Register your models here.
admin.site.register(Tag)
