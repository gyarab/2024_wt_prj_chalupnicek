from django.shortcuts import render

from main.models import Movie

def get_homepage(request):
    movies = Movie.objects.all().order_by('title')

    # check if search parameter is in the request
    if request.GET.get("search"):
        movies = movies.filter(title__icontains=request.GET.get("search"))

    context = {
        "svatek": "Libor",
        # SELECT * from Movies ORDER BY 'title' LIMIT 10;
        "movies": movies
    }
    return render(
        request, "main/homepage.html", context
    )
