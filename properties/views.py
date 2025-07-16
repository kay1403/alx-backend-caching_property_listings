from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties  # or directly query Property

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()  # returns list of dicts
    # Return the list directly, safe=False allows top-level arrays
    return JsonResponse(properties, safe=False)
