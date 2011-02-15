from django.contrib import admin
from models import Library, Resource, Book, Technology

class LibraryAdmin(admin.ModelAdmin):
  class Media:
    js = ('js/tiny_mce/tiny_mce_src.js',
          'js/tiny_mce/textareas.js')

admin.site.register(Library, LibraryAdmin)
admin.site.register(Book)
admin.site.register(Technology)
