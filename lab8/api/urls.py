from django.urls import path, re_path
from . import views

urlpatterns = [
    path('products/',views.listAllProductsHandler),
    path('categories/',views.listAllCategoriesHandler),
    path('products/<int:pk>/',views.listOneProductHandler),
    path('categories/<int:pk>/',views.listOneCategoryHandler),
    path('categories/<int:pk>/products/',views.listProductsByCategoryIdHandler)
]