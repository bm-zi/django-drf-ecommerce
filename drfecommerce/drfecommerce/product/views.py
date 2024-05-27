from django.db import connection
from django.db.models import Prefetch
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers.sql import SqlLexer
from sqlparse import format

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all the categories
    """
    
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all brands
    """
    
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
class ProductViewSet(viewsets.ViewSet):
    """
    Viewset for viewing all products
    """
    
    queryset = Product.objects.all().isactive()
    lookup_field = "slug"
    
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            self.queryset.filter(slug=slug)
            .select_related("category", "brand")
            .prefetch_related(Prefetch("product_line__product_image")), 
            many=True
        )
        
        data =  Response(serializer.data)
        ### 
        q = list(connection.queries)
        print(len(q))
        for qs in q:
            sqlformatted = format(str(qs["sql"]), reindent=True)
            print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        ###
        return data

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<slug>[\w-]+)",
    )
    def list_product_by_category(self, request, slug=None):
        """
        An endpoint to return products by category
        """
        serializer = ProductSerializer(self.queryset.filter(category__slug=slug), many=True)
        return Response(serializer.data)