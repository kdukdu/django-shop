from django.urls import path

from .views import ProductApiView, ProductApiDetailView

urlpatterns = [
    path('product/list/', ProductApiView.as_view()),
    path('product/<int:pk>/detail/', ProductApiDetailView.as_view()),
]
