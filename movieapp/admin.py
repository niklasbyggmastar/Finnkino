from django.contrib import admin
from .models import Movie, Review, Theatre, Auditorium, Show, Ticket

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Theatre)
admin.site.register(Auditorium)
admin.site.register(Show)
admin.site.register(Ticket)
