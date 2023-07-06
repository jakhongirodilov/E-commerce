from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:product_id>', views.product, name='product'),
    path('new_product/', views.new_product, name='new_product'),
    path('update_product/<int:product_id>', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
    path('my_products/', views.my_posts, name='my_products'),
    path('add/<int:product_id>', views.add, name='add'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('search/', views.search, name='search'),
    path('category/', views.display_category, name='display_category')
]