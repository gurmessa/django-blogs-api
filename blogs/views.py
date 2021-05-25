from django.shortcuts import render
from rest_framework import viewsets #,generics,permissions 

from .models import Blog
from .serializers import BlogSerializer
from .permissions import IsAuthorOrReadOnly


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly,]



"""
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes =  (IsAuthorOrReadOnly,)
"""