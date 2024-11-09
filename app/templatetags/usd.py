from django import template
register=template.Library()

def swap(value):
    return value.swapcase()
register.filter('swapping',swap)

def splitting(value,arg):
    return value.split(arg)
register.filter('splitting',splitting)
@register.filter()
def reverse(value):
    return " ".join(value.split()[::-1])
# register.filter('reverse',reverse)