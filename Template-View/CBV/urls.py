from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'website'

urlpatterns = [
    # extra_context Attribute from ContentMixin - keyword argument for as_view()
    path('ex1', views.TemplateView.as_view(template_name="ex1.html",extra_context={'title': 'Custom Title'})),
    path('ex2', views.Ex2View.as_view(), name='ex2'),
]