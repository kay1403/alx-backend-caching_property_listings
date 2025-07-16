from django.core.cache import cache
from .models import Property

def getallproperties():
    properties = cache.get('allproperties')
    if not properties:
        properties = list(Property.objects.all().values())
        cache.set('allproperties', properties, 3600)  # 3600 secondes = 1 heure
    return properties
