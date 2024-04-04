from django import template

register = template.Library()


@register.filter()
def to_string(value: int):
    return str(value)
