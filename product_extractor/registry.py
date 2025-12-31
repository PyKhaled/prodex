from product_extractor.adapters.generic import GenericAdapter
from product_extractor.adapters.shopify import ShopifyAdapter
from product_extractor.adapters.amazon import AmazonAdapter
ADAPTERS = [
    ShopifyAdapter,
    AmazonAdapter,
]


def resolve_adapter(url: str):
    for adapter_cls in ADAPTERS:
        if adapter_cls.matches(url):
            return adapter_cls()
    return GenericAdapter()