from django import template

register = template.Library()

from ..models import PageContent

@register.simple_tag
def get_content(arg):
    try:
        # return PageContent.objects.all().count()
        obj = PageContent.objects.get(title=arg)
        desc = obj.description
        return desc
    except:
        return "Kindly add content with title " + arg