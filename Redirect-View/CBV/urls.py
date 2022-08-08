from django.urls import path
from django.views.generic import RedirectView
from .views import PostPreLoadTaskView, SinglePostView

app_name = 'cbv'

urlpatterns = [
    path('rdt', RedirectView.as_view(url='https://www.google.com/'),name='go-to-very'),
    path('e1/<int:pk>/', PostPreLoadTaskView.as_view(), name='redirect-task'),
    path('e2/<int:pk>/', SinglePostView.as_view(),name='singlepost'),  # single post page
]