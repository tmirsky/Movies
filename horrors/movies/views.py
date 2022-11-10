from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import ReviewForm
from .models import Movie, Actor, Director


class ContextMixin:

    context = {
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'googleplus': 'https://gmail.com',
        'youtube': 'https://youtube.com',
    }


class MoviesView(ContextMixin,ListView):
    #Список фильмов
    model = Movie
    template_name = 'movies/index.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MoviesView, self).get_context_data(**kwargs)
        context.update(self.context)
        context['user'] = self.request.user
        return context


class MoviesListView(ContextMixin, ListView):
    #Список фильмов
    model = Movie
    template_name = 'movies/movies_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MoviesView, self).get_context_data(**kwargs)
        context.update(self.context)
        context['user'] = self.request.user
        return context


class MovieDetailView(DetailView):
   #Полное описание фильмов
    model = Movie
    slug_field = 'url'

    def get_queryset(self):
        return Movie.objects.filter(is_published=True)

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

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


class AddReview(LoginRequiredMixin, View):
    #Отзывы

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
