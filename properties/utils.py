from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging

def get_all_properties():
    properties = cache.get('all_properties')
    if not properties:
        properties = list(Property.objects.all().values())
        cache.set('all_properties', properties, timeout=3600)
    return properties


logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    conn = get_redis_connection("default")
    info = conn.info()
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    hit_ratio = (hits / total) * 100 if total else 0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": f"{hit_ratio:.2f}%"
    }

    logger.info("Redis Cache Metrics: %s", metrics)
    return metrics
