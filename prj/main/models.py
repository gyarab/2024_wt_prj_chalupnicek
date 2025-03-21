from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, default="")
    director = models.ForeignKey('Director', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title} ({self.year})"

class Director(models.Model):
    name = models.CharField(max_length=300)
    birth_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.name} ({self.birth_year})"

