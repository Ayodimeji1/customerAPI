from django.urls import path
from customerApp import views

urlpatterns = [
    path('customers/', views.CustomerListView.as_view()),
    path('customers/<int:pk>', views.CustomerDetailView.as_view()),
    path('orders/', views.OrderListView.as_view()),
    path('orders/<int:pk>', views.OrderDetailView.as_view()),
]
