import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import (
    BrandFactory,
    CategoryFactory,
    ProductFactory,
    ProductImageFactory,
    ProductLineFactory,
    AttributeFactory,
    ProductTypeFactory,
    AttributeValueFactory,
)

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductLineFactory)
register(ProductImageFactory)
register(AttributeFactory)
register(ProductTypeFactory)
register(AttributeValueFactory)


@pytest.fixture
def api_client():
    return APIClient
