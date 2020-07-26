from django.contrib import admin

from .models import Category, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    readonly_fields = ['thumb',]

class PhotoModel(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Category, PhotoModel)