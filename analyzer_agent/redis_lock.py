import redis
r = redis.Redis()


def acquire_lock(key):
    return r.setnx(f"lock:{key}", 1)


def release_lock(key):
    r.delete(f"lock:{key}")