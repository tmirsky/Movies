from django.urls import path

from .views import MoviesView, MovieDetailView, Search, ActorView, DirectorView, AddReview, MoviesListView


urlpatterns = [
    path("", MoviesView.as_view(), name='index'),
    path("", MoviesListView.as_view(), name='movie_list'),
    path("search/", Search.as_view(), name='search'),
    path("<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", ActorView.as_view(), name="celebrities"),
    path("director/<str:slug>/", DirectorView.as_view(), name="celebrities"),
]