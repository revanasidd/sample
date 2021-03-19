from django.urls import path

from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('products',views.products,name='products'),
	path('customer/<str:pk>/',views.Customers,name='customer'),
	path('create_order',views.Createorder,name='create_order'),
	path('updateorder/<str:pk>/',views.updateOrder,name='updateorder'),
	path('deleteorder/<str:pk>/',views.deleteOrder,name='deleteorder'),
]