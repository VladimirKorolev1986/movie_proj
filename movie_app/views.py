from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


# Create your views here.


def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('Hello'),
        int_field=Value(3),
        new_budjet=F('budget') + 100,
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movie.html', {
        'movies': movies,
        'agg': agg,
        'count': movies.count()
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors
    })


def one_director(request, id_director: int):
    directors = get_object_or_404(Director, id=id_director)
    return render(request, 'movie_app/one_director.html', {
        'directors': directors,
    })


def all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors,
    })


def one_actor(request, id_actor: int):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, 'movie_app/one_actor.html', {
        'actor': actor,
    })

