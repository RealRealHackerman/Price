from django.urls import path
from . import views

urlpatterns = [
    path("", views.price, name="price"),
    path("price/<str:symbol>/", views.price_detail, name="price_detail"),
]