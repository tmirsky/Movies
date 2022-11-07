from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Actor, Director


class ContextMixin:

    context = {
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'gmail': 'https://gmail.com',
    }


class MoviesView(ListView):
    #Список фильмов
    model = Movie
    paginate_by = 1

    def get_queryset(self):
        return Movie.objects.filter(is_published=False)


class MovieDetailView(DetailView):
   #Полное описание фильмов
    model = Movie
    slug_field = 'url'

    def get_queryset(self):
        return Movie.objects.filter(is_published=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ActorView(DetailView):
    # Вывод информации о актере
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'


class DirectorView(DetailView):
    # Вывод информации о режиссере
    model = Director
    template_name = 'movies/director.html'
    slug_field = 'name'


class Search(ListView):
    # Поиск фильмов
    paginate_by = 3

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
