from jasonkotenko.library.models import Library
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
def show_library(request, req_name):
  library = get_object_or_404(Library, name=req_name)
  
  return render_to_response('library/library.html', {'library': library})
