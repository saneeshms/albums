from django.views import generic
from music.models import Album
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model=Album
    fields = ['artist','album_title','genre','logo']

class AlbumUpdate(UpdateView):
    model=Album
    fields = ['artist','album_title','genre','logo']

class AlbumDelete(DeleteView):
    model=Album
    success_url=reverse_lazy('music:index')


























