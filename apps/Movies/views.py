from django.shortcuts import render
from rest_framework import generics
from .models import Movies
from .serializers import MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



class MovieList(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields ={'category_id': ['exact']}
    search_fields = ['title', 'description']
    
class MovieDetail(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class= MovieSerializer
    