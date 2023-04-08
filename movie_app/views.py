from django.shortcuts import render


# Create your views here.


def show_all_movie(request):
    return render(request, 'movie_app/all_movie.html')
