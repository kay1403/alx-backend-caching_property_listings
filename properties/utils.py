from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    conn = get_redis_connection("default")
    info = conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total_requests = hits + misses

    if total_requests > 0:
        hit_ratio = (hits / total_requests) * 100
    else:
        hit_ratio = 0.0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": f"{hit_ratio:.2f}%"  # format en string pour affichage lisible
    }

    logger.info("Redis Cache Metrics: %s", metrics)
    return metrics
