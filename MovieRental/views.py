from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from Movies.models import Movies
from Movies.serializers import MoviesSerializer


def homePage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if User.objects.filter(username=username).exists():
            login(request, user)
            return redirect("/movies/all/")
        else:
            return HttpResponse("<h1>Invalid Details</h1>")
    else:
        return render(request,"homepage.html")


def log_out(request):
    logout(request)
    return render(request,"homepage.html")

class movieViewSet(APIView):

    def get(self, request):

        queryset = Movies.objects.all()
        serializer= MoviesSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class movieGet(APIView):
    def get(self,request,movie_id):
        queryset1 = Movies.objects.get(id=movie_id)
        serializer = MoviesSerializer(queryset1)
        return Response(serializer.data)

    def delete(self, request, movie_id):
        queryset2 = Movies.objects.get(id=movie_id)
        queryset2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
