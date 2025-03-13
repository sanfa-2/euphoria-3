from django import template

register = template.Library()

@register.filter
def range_filter(value):
    """ Returns a range from 0 to value """
    try:
        return range(value)
    except TypeError:
        return []  # In case 'value' is not an integer.
