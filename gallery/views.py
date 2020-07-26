from .models import Photo, Category
from .serializers import CategorySerializer, PhotoSerializer
from rest_framework import generics
import django_filters.rest_framework

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PhotoList(generics.ListAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        id = self.kwargs['category_id']
        return Photo.objects.filter(category=id)

class TopPhotoList(generics.ListAPIView):
    queryset = Photo.objects.filter(top=True)
    serializer_class = PhotoSerializer