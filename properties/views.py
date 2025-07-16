from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties

@cache_page(60 * 15)  # Cache la réponse complète pendant 15 minutes
def property_list(request):
    properties = get_all_properties()  # Utilise le cache bas niveau pour la queryset
    return JsonResponse(properties, safe=False)
