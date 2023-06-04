from django import template
from django.conf import settings

register = template.Library()


@register.filter
def media_path(image_path):

    return f"{settings.MEDIA_URL}{image_path}"