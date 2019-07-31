from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from pip._vendor.requests import Response
from rest_framework import viewsets
from Customer.models import Customer
from rest_framework.views import APIView
from Movies.serializers import MoviesSerializer
from . import form


from Movies.models import Movies


@login_required(login_url="homepage")
def movies(request, order_by='name'):
    moviename = Movies.objects.all().order_by(order_by)
    return render(request, "movies.html", {

        "moviename": moviename
    })


def movies_delete(request, movie_id):
    d = Movies.objects.get(id=movie_id)

    d.delete()

    return redirect('/movies/all')

@login_required(login_url="homepage")
def movies_add(request):
    if request.method == 'POST':
        form1 = form.addMovie(request.POST)
        if form1.is_valid():
            # name = form1.cleaned_data["name"]
            # actor = form1.cleaned_data["actor"]
            # year = form1.cleaned_data["year"]
            # genre = form1.cleaned_data["genre"]
            # price = form1.cleaned_data["price"]
            # m = Movies(name=name, actor=actor, year=year, genre=genre, price=price)
            # m.save()
            # return redirect('/movies/all')
            j = form1.save(commit=False)
            j.save()
            return redirect('/movies/all')
    else:
        form1 = form.addMovie()

    return render(request, 'addmovie.html', {
        "form": form1
    })

@login_required(login_url="homepage")
def movies_available(request, order_by='name'):
    availablename = Movies.objects.filter(rented__isnull=True).order_by(order_by)

    return render(request, "available.html", {

        "availablename": availablename
    })

@login_required(login_url="homepage")
def movies_rented(request, order_by='name'):
    rentedname = Movies.objects.filter(rented__isnull=False).order_by(order_by)
    return render(request, "rented.html", {
        "rentedname": rentedname
   })

def movies_update(request,movie_id):
    update_data = Movies.objects.get(id=movie_id)
    if request.method == 'POST':
        form1 = form.addMovie(request.POST , instance=update_data)
        if form1.is_valid():
            j = form1.save(commit=False)
            j.save()
            return redirect('/movies/all')
    else:
        form1 = form.addMovie(instance=update_data)

    return render(request, 'updatemovie.html', {
        "form": form1
    })


class assignmovie(TemplateView):
    template_name = "assignmovie.html"

    @method_decorator(login_required(login_url="homepage"))
    def get(self,request):

        movie=Movies.objects.filter(rented__isnull=True)
        customer=Customer.objects.all()

        return render(request,"assignmovie.html",{
            "moviedata": movie , "customerdata": customer
        })

    def post(self, request):
        a=Movies.objects.get(id=request.POST["movie_id"])
        b=Customer.objects.get(id=request.POST["customer_id"])

        a.rented=b
        a.save()

        return render(request,"assignmovie.html")


#
# class movieViewSet(APIView):
#
#     def get(self, request):
#
#         queryset = Movies.objects.all()
#         serializer_class = MoviesSerializer(queryset,many=True)
#         return Response(serializer_class.data)
#
#     def post(self):
#         pass