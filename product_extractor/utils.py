import hashlib


def make_cache_key(url: str, soft: bool) -> str:
    raw = f"{url}|soft={soft}"
    return hashlib.sha256(raw.encode()).hexdigest()
