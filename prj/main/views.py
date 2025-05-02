from django.shortcuts import render

from main.models import Movie

def get_homepage(request):
    movies = Movie.objects.all().order_by('title')
    
    # filter by title if query parameter search is present
    search = request.GET.get('search')
    if search:
        movies = movies.filter(description__icontains=search)

    context = {
        "svatek": "Libor",
        # SELECT * from Movies ORDER BY 'title' LIMIT 10;
        "movies": movies
    }
    return render(
        request, "main/homepage.html", context
    )
