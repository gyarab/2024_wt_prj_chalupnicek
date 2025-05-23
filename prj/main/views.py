from django.shortcuts import render
from faker import Faker
from django.http import HttpResponse

from main.models import Movie, Genre

def get_homepage(request):
    movies = Movie.objects.all().order_by('name')
    
    # filter by name if query parameter search is present
    search = request.GET.get('search')
    if search:
        movies = movies.filter(name__icontains=search) | movies.filter(description__icontains=search)

    # filter by genre if query parameter genre is present
    genre = request.GET.get('genre')
    if genre:
        movies = movies.filter(genres__name=genre)
    
    context = {
        # SELECT * from Movies ORDER BY 'name' LIMIT 10;
        "movies": movies,
        "genres": Genre.objects.all().order_by('name'),
        "genre": genre,
    }
    return render(
        request, "main/homepage.html", context
    )

def get_movie(request, id):
    print(id)
    # SELECT * from Movies WHERE id = id;
    movie = Movie.objects.get(id=id)
    context = {
        "movie": movie
    }
    return render(
        request, "main/movie.html", context
    )

def random_person(request):
    context = {
        # use faker to generate random data
        "name": Faker().name(),
        "email": Faker().email(),
        "phone": Faker().phone_number(),
   }
    return render(
        request, "main/random.html", context
    )

def add_like(request, movie_id):
    # movie_id = request.GET.get('movie_id')
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return HttpResponse(status=404, content='{"status": "error", "message": "Movie not found"}', content_type="application/json")
    if not movie.likes:
        movie.likes = 0
    movie.likes += 1
    movie.save()
    return HttpResponse(status=200, content='{"status": "ok", "likes": "'+str(movie.likes)+'"}', content_type="application/json")