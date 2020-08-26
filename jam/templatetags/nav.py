from django.template import Library

from jam.models import Genre


register = Library()


@register.inclusion_tag('jam/nav_tpl.html')
def get_genres():
    genres = Genre.objects.all()
    return {"genres": genres}