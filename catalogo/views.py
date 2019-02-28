from django.shortcuts import render
from catalogo.models import Movie

# Create your views here.

def catalog_view(request):
    movies = Movie.objects.all() # Pega todos os objetos salvos no banco
    context = {
        'movies': movies
    }
    return render(request, 'catalog.html', context)