from django import template
from geonode.maps.models import Map

register = template.Library()

# Map snippets
@register.inclusion_tag('maps/maps.html', takes_context=True)
def maps(context):
	print("QUI \n")
	return {
		'maps': Map.objects.all(),
		'request': context['request'],
	}