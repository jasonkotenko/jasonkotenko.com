from django.utils.encoding import force_unicode
from django import template
from thatgaljam import settings
import re, os, Image, random, posixpath
register = template.Library()  


@register.inclusion_tag('_paginator.html')
def paginator(object):
    return {'object': object}

@register.filter("truncate_chars")  
def truncate_chars(value, max_length):  
   if len(value) <= max_length:  
       return value  
 
   truncd_val = value[:max_length]  
   if value[max_length] != " ":  
      rightmost_space = truncd_val.rfind(" ")  
      if rightmost_space != -1:  
           truncd_val = truncd_val[:rightmost_space]  
 
   return truncd_val + "..."   
   
@register.filter("striptags_spaces")
def strip_tags(value):
	"""Returns the given HTML with all tags stripped."""
	return re.sub(r'<[^>]*?>', ' ', force_unicode(value))

@register.filter("thumbnail")
def thumbnail(file, size='100x60'):
    # defining the size
    x, y = [int(x) for x in size.split('x')]
    # defining the filename and the miniature filename
    filehead, filetail = os.path.split(file.path)
    basename, format = os.path.splitext(filetail)
    miniature = basename + '_' + size + format
    filename = file.path
    miniature_filename = os.path.join(filehead, miniature)
    filehead, filetail = os.path.split(file.url)
    miniature_url = filehead + '/' + miniature
    if os.path.exists(miniature_filename) and os.path.getmtime(filename)>os.path.getmtime(miniature_filename):
        os.unlink(miniature_filename)
    # if the image wasn't already resized, resize it
    if not os.path.exists(miniature_filename):
        image = Image.open(filename)
        image.thumbnail([x, y], Image.ANTIALIAS)
        try:
            image.save(miniature_filename, image.format, quality=90, optimize=1)
        except:
            image.save(miniature_filename, image.format, quality=90)

    return miniature_url
    
@register.filter("sthumbnail")
def pilthumb(file, size='75x75'):
    # defining the size
    x, y = [int(x) for x in size.split('x')]
    # defining the filename and the miniature filename
    filehead, filetail = os.path.split(file.path)
    basename, format = os.path.splitext(filetail)
    miniature = basename + '_' + size + format
    filename = file.path
    miniature_filename = os.path.join(filehead, miniature)
    filehead, filetail = os.path.split(file.url)
    miniature_url = filehead + '/' + miniature
    if os.path.exists(miniature_filename) and os.path.getmtime(filename)>os.path.getmtime(miniature_filename):
        os.unlink(miniature_filename)
    # if the image wasn't already resized, resize it
    if not os.path.exists(miniature_filename):
        image = Image.open(filename)
        width, height = image.size
        
        if width > height:
            delta = width - height
            left = int(delta/2)
            upper = 0
            right = height + left
            lower = height
        else:
            delta = height - width
            left = 0
            upper = int(delta/2)
            right = width
            lower = width + upper
        image = image.crop((left, upper, right, lower))
        
        image.thumbnail([x, y], Image.ANTIALIAS)
        try:
            image.save(miniature_filename, image.format, quality=90, optimize=1)
        except:
            image.save(miniature_filename, image.format, quality=90)

    return miniature_url

def is_image_file(filename):
    """Does `filename` appear to be an image file?"""
    img_types = [".jpg", ".jpeg", ".png", ".gif"]
    ext = os.path.splitext(filename)[1].lower()
    return ext in img_types

@register.simple_tag
def random_image(path):
    """
    Select a random image file from the provided directory
    and return its href. `path` should be relative to MEDIA_ROOT.
    
    Usage:  <img src='{% random_image "images/whatever/" %}'>
    """
    print path
    print settings.MEDIA_ROOT
    fullpath = os.path.join(settings.MEDIA_ROOT, path)
    print fullpath
    filenames = [f for f in os.listdir(fullpath) if is_image_file(f)]
    print filenames
    pick = random.choice(filenames)
    return posixpath.join(settings.MEDIA_URL, path, pick)
