from django.shortcuts import render
from rest_framework import generics,permissions 

from .models import Blog
from .serializers import BlogSerializer
from .permissions import IsAuthorOrReadOnly


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes =  (IsAuthorOrReadOnly,)
