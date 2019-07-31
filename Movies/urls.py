from django.contrib import admin
from django.urls import path

from Movies import views
from Movies.views import assignmovie

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('all/', views.movies, name="movies"),
    path('delete/<movie_id>/',views.movies_delete, name="deleteMovie"),
    path('add/',views.movies_add, name="addmovie"),
    path('available/',views.movies_available, name="availablemovie"),
    path('rented/',views.movies_rented, name="rentedmovie"),
    path('assign/',assignmovie.as_view(), name="assign"),
    path('update/<movie_id>/',views.movies_update,name="updatemovie"),

]
