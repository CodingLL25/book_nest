from django import template
from django.utils.html import strip_tags
import re

register = template.Library()


@register.filter(name="clean_html")
def clean_html(value):
    if not value:
        return ""
    value = re.sub(r"<p[^>]*>\s*(?:&nbsp;|\s)*</p>", "", value)
    value = re.sub(r"&nbsp;", " ", value)
    return strip_tags(value).strip()
