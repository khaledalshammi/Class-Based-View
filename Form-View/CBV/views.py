from django.views.generic.edit import FormView
from .forms import AddForm

class AddBookView(FormView):
    template_name = 'add.html'
    form_class = AddForm
    success_url = '/books/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)