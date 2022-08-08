from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('g/<str:genre>', views.GenreView.as_view(), name='genre'),
]