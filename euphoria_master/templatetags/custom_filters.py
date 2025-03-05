# euphoria/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def range_filter(value):
    # Make sure the value passed is an integer
    if isinstance(value, int):
        return range(value)
    return []  # Return an empty list if the value is not an integer
