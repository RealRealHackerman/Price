from django import template

register = template.Library()


@register.filter
def price_format(value):

    if value is None or value == "":
        return "-"

    try:
        value = float(value)
    except (ValueError, TypeError):
        return "-"

    value = int(value) // 10
    return f"{value:,}"
@register.filter
def change_class(value):
    value = float(value)

    if value > 0:
        return "positive"
    elif value < 0:
        return "negative"

    return "neutral"


@register.filter
def change_sign(value):
    value = float(value)

    if value > 0:
        return f"+{value}"

    return str(value)