from django.views.generic.edit import CreateView
from .models import Books,Core
from .forms import AddForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView

class AddBookView(CreateView):
    model = Books
    form_class = AddForm
    template_name = 'add.html'
    success_url = '/books/'

class EditView(UpdateView):
    model = Core
    template_name = 'core/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('posts')