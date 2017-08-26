from django.db import models
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=30)
    released = models.DateTimeField('date published')
    genre = models.CharField(max_length=15, default="")
    duration_mins = models.IntegerField(default=0)
    description = models.CharField(max_length=300, default="")
    poster = models.ImageField(upload_to="static/img", default="")

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    released = models.DateTimeField('date published', default=timezone.now)
    stars = models.IntegerField(default=0)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment

class Theatre(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name

class Auditorium(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    number_of_rows = models.IntegerField(default=0)
    number_of_cols = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE, default="")
    city = models.CharField(max_length=50, default="")
    show_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.movie.title

class Ticket(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user_id = models.IntegerField(default=0)
    seat_row = models.IntegerField(default=0)
    seat_col = models.IntegerField(default=0)

    def __str__(self):
        return self.show.movie.title
