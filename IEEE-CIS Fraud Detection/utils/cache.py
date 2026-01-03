from cachetools import TTLCache

prediction_cache = TTLCache(maxsize=100_000, ttl=3600)
