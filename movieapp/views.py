from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q

from .models import Movie, Review, Theatre, Auditorium, Show, Ticket
from .forms import SignUpForm

def index(request):
    latest_movies = Movie.objects.all().order_by('-id')[:12]
    context = {'latest_movies': latest_movies}
    return render(request, 'movieapp/index.html', context)

def info(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movieID = movie.id
    released = movie.released
    genre = movie.genre
    duration_mins = movie.duration_mins
    description = movie.description
    poster = movie.poster
    all_reviews = movie.review_set.all().order_by('-id')
    all_shows = movie.show_set.all().order_by('-city')
    context = {"movieID": movieID, "title":movie, "released": released, "genre": genre, "duration_mins": duration_mins, "description": description, "poster": poster, "all_reviews": all_reviews, "all_shows": all_shows}
    return render(request, 'movieapp/info.html', context)

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("raw_password")
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Signup successful!', extra_tags="alert-success text-center")
            return redirect("../")
    else:
        form = SignUpForm()
    return render(request, "movieapp/signup.html", {"form": form})


def profile(request):
    user_id = request.user.id
    my_tickets = Ticket.objects.filter(user_id=user_id)
    context = {"my_tickets": my_tickets}
    return render(request, "movieapp/profile.html", context)

def theatres(request):
    all_theatres = Theatre.objects.all().order_by('-city')
    context = {"all_theatres": all_theatres}
    return render(request, "movieapp/theatres.html", context)

def movies_by_genre(request, movie_genre):
    all_movies = Movie.objects.filter(genre=movie_genre).order_by('-id')
    genre = movie_genre
    context = {"all_movies": all_movies, "genre": genre}
    return render(request, "movieapp/movies.html", context)

def shows_by_city(request, city_name):
    all_shows = Show.objects.filter(city=city_name).order_by('-id')
    city = city_name
    context = {"all_shows": all_shows, "city": city}
    return render(request, "movieapp/shows.html", context)

def buy(request):
    show_id = request.POST['showID']
    show = Show.objects.get(pk=show_id)
    bought_tickets = show.ticket_set.all()
    loop_cols = range(1, show.auditorium.number_of_cols + 1)
    loop_rows = range(1, show.auditorium.number_of_rows + 1)
    context = {"show": show, "show_id": show_id, "loop_cols": loop_cols, "loop_rows": loop_rows, "bought_tickets": bought_tickets}
    return render(request, "movieapp/buy.html", context)

def search(request):
    search_text = request.POST['text']
    results = Movie.objects.filter(Q(title__startswith=search_text) | Q(genre__startswith=search_text))
    context = {"search_text": search_text, "results": results}
    return render(request, "movieapp/search.html", context)


#---------------------------------Pelkät toiminnot------------------------------------
def login_view(request):
    username=request.POST['username']
    password=request.POST['password']
    next = request.POST.get('next', '/')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'Login successful!', extra_tags="alert-success text-center")
        return HttpResponseRedirect(next)
    else:
        messages.warning(request, 'Username or password is incorrect!', extra_tags="alert-danger text-center")
        return HttpResponseRedirect(next)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful!', extra_tags="alert-success text-center")
    return redirect("../")

def post_comment(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    username = request.user.username
    stars = request.POST['stars']
    comment = request.POST['comment']
    movie.review_set.create(user=username, released=timezone.now(), stars=stars, comment=comment)
    next = request.POST.get('next', '/')
    messages.success(request, 'Review posted!', extra_tags="alert-success text-center")
    return HttpResponseRedirect(next)

def buy_tickets(request):
    showID = request.POST['showID']
    show = Show.objects.get(pk=showID)
    user = request.user.id
    seat_row = request.POST['seat_row']
    seat_col = request.POST['seat_col']
    ticket = Ticket(show=show, user_id=user, seat_row=seat_row, seat_col=seat_col)
    ticket.save()
    messages.success(request, 'Purchase successful!', extra_tags="alert-success text-center")
    return redirect("../")

def remove_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.delete()
    next = request.POST.get('next', '/')
    messages.success(request, 'Ticket deleted!', extra_tags="alert-success text-center")
    return HttpResponseRedirect(next)

def change_password(request):
    next = request.POST.get('next', '/')
    old_password = request.POST['old_password']
    user = authenticate(username=request.user.username, password=old_password)
    if user is not None:
        new_password = request.POST['new_password']
        new_password2 = request.POST['new_password2']
        if new_password == new_password2:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password change successful!', extra_tags="alert-success text-center")
        else:
            messages.warning(request, 'The new password fields did not match!', extra_tags="alert-danger text-center")
    else:
        messages.warning(request, 'Incorrect password!', extra_tags="alert-danger text-center")
    return HttpResponseRedirect(next)
