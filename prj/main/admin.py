from django.contrib import admin
from .models import Movie, Director

class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "year", "director"]

class DirectorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year"]

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)