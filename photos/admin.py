from django.contrib import admin
from models import Gallery, Photo, GalleryUpload

class PhotoInline(admin.TabularInline):
  model = Photo

class GalleryAdmin(admin.ModelAdmin):
  inlines = [
    PhotoInline,
  ]
  
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo)
admin.site.register(GalleryUpload)
