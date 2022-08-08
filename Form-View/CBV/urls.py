from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('add/', views.AddBookView.as_view(), name='add'),
]