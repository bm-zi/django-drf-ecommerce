import factory

from drfecommerce.product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = factory.Sequence(lambda n: "Category_%d" % n)
    
    # populate data for specific fields 
    # name = "test_category"


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
    
    # populate data for specific fields 
    name = "test_brand"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        
    name = "test_product"
    description = "test_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)