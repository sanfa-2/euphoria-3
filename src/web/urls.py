from django.urls import path
from . import views  

app_name = 'web'

urlpatterns = [
    path("", views.index, name="index"),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path("category/<int:category_id>/", views.category_products, name="category_products"),
    path("categories/men/", views.men_categories, name="men_categories"),
    path("categories/women/", views.women_categories, name="women_categories"),
    path('search/', views.search, name='search'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wish-cart/', views.wish_cart_view, name='wish_cart_view'), 
    path('wish-cart/add/<int:product_id>/', views.add_to_wish_cart, name='add_to_wish_cart'), 
    path('wish-cart/remove/<int:product_id>/', views.remove_from_wish_cart, name='remove_from_wish_cart'),  
    
]
