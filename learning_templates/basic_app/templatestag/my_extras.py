# First we need to register all of tHis
from django import templates

# Then we set  an  aobject
register = templates.Library()
#
# we then have to write a function that will be custom templates filter
@register.filter(name="cut")
def cut(value,arg):
    """

   This cuts out all the values of "arg" form the string!
    """
    return value.replace(arg,"")

# Then we need to register tHis
# register.filter("cut",cut)
