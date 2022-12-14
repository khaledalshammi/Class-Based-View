from django.views.generic.list import ListView
from .models import Books
from django.utils import timezone

class IndexView(ListView):
    model = Books
    template_name = 'home.html'
    context_object_name = 'books'
    paginate_by = 1  # Pagination over-write
    # queryset = Books.objects.all()[:2]
    # queryset = Books.objects.filter(title='')
    #Alturnative override class methods.
    #def get_queryset(self):
        #return Books.objects.all()[:3]
    #Alturnative override class methods.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = timezone.now()
        return context

class GenreView(ListView):
    model = Books
    template_name = 'home.html'
    context_object_name = 'books'
    paginate_by = 2  # Pagination over-write
    def get_queryset(self, *args, **kwargs):
        return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))