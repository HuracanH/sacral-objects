from django.shortcuts import render
from django.views.generic import ListView

from movie.models import Movie

class MovieList(ListView):
    model = Movie
