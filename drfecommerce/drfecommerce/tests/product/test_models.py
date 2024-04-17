import pytest


# Provide access to databse django_db globally for all tests in this file
pytestmark = pytest.mark.django_db 

class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        obj = category_factory(name="test_cat")   # overide the name
        # Assert 
        assert obj.__str__() == "test_cat"

class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        obj = brand_factory(name="test_brand")   # overide the name
        # Assert 
        assert obj.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        obj = product_factory(name="test_product")   # overide the name
        # Assert 
        assert obj.__str__() == "test_product"