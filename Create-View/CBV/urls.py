from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddBookView.as_view(), name='add'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
]