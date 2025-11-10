from django.contrib import admin
from .models import Collection, Book, Tag
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.admin import SimpleListFilter
from django.utils.html import strip_tags


def clean_html(text):
    return strip_tags(text)


class TagFilter(SimpleListFilter):
    title = "Tag"  # name of the filter
    parameter_name = "tag"

    def lookups(self, request, model_admin):  # populate dropdown filter options
        return [(tag.id, tag.name) for tag in Tag.objects.all()]  # as tuples

    def queryset(self, request, queryset):  # filtering logic
        if self.value():  # return selected tag ID
            return queryset.filter(books__tag__id=self.value()).distinct()
        return queryset


@admin.register(Collection)
class Collection(SummernoteModelAdmin):

    list_display = ("name", "theme", "excerpt_clean")
    search_fields = ["theme", "excerpt"]
    list_filter = (TagFilter, "theme")
    summernote_fields = ("excerpt",)

    @admin.display(description="excerpt")
    def excerpt_clean(self, obj):
        return clean_html(obj.excerpt)


# error with filtering the book by tag
@admin.register(Book)
class Book(SummernoteModelAdmin):

    list_display = ("title", "author", "body_clean")
    search_fields = ["title", "author"]
    list_filter = (TagFilter, "author")
    summernote_fields = ("body",)

    @admin.display(description="body")
    def body_clean(self, obj):
        return clean_html(obj.body)


# Register your models here.
admin.site.register(Tag)
