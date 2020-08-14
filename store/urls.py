from django.urls import path

from . import views

urlpatterns = [

    # Leave as empty string for base url

	path('', views.store, name="store"),
	path('about/', views.about, name="about"),
	# path('blog/', views.blog, name="blog"),
	# path('blog-details/', views.blog-details, name="blog-details"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('confirmation/', views.confirmation, name="confirmation"),
	path('contact/', views.contact, name="contact"),
	path('product_details/', views.product_details, name="product_details"),
	path('login/', views.login, name="login"),
	path('shop/', views.shop, name="shop"),

]