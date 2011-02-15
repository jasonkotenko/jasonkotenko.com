from jasonkotenko.photos.models import Gallery, Photo
from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404

def gallery(request, req_name):
  gallery = get_object_or_404(Gallery, name=req_name)
  return render_to_response('photos/gallery.html', \
                            {'gallery': gallery})

def gallery_list(request):
  galleries = Gallery.objects.all()
  return render_to_response('photos/gallery_list.html', \
                            {'galleries': galleries})
