from django.db import models

import os
import zipfile
from django.core.files.base import ContentFile

class Photo(models.Model):
  image = models.ImageField(upload_to="images")
  title = models.CharField(max_length=128, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  gallery = models.ForeignKey("Gallery")

  def __unicode__(self):
    return self.title

class Gallery(models.Model):
  name = models.CharField(max_length=128)
  description = models.TextField()
  created = models.DateField(auto_now_add=True)
  
  def __unicode__(self):
    return self.name


# Required PIL classes may or may not be available from the root namespace
# depending on the installation method used.
try:
    import Image
    import ImageFile
    import ImageFilter
    import ImageEnhance
except ImportError:
    try:
        from PIL import Image
        from PIL import ImageFile
        from PIL import ImageFilter
        from PIL import ImageEnhance
    except ImportError:
        raise ImportError('Unable to import the Python Imaging Library. Please confirm it`s installed and available on your current Python path.')

from jasonkotenko.settings import MEDIA_ROOT

#Thanks to django-photologue
class GalleryUpload(models.Model):
    zip_file = models.FileField(upload_to=MEDIA_ROOT+"/temp",
               help_text='Select a .zip file of images to upload into a new Gallery.')
    gallery = models.ForeignKey(Gallery, null=True, blank=True, 
               help_text='Select a gallery to add these images to. leave this empty to create a new gallery from the supplied title.')
    name = models.CharField(max_length=75, help_text='All photos in the gallery will be given a title made up of the gallery title + a sequential number.')
    description = models.TextField(blank=True, help_text='A description of this Gallery.')

    class Meta:
        verbose_name = 'gallery upload'
        verbose_name_plural = 'gallery uploads'

    def save(self, *args, **kwargs):
        super(GalleryUpload, self).save(*args, **kwargs)
        gallery = self.process_zipfile()
        super(GalleryUpload, self).delete()
        return gallery

    def process_zipfile(self):
        if os.path.isfile(self.zip_file.path):
            # TODO: implement try-except here
            zip = zipfile.ZipFile(self.zip_file.path)
            bad_file = zip.testzip()
            if bad_file:
                raise Exception('"%s" in the .zip archive is corrupt.' % bad_file)
            count = 1
            if self.gallery:
                gallery = self.gallery
            else:
                gallery = Gallery.objects.create(name=self.name,
                                                 description=self.description)
            from cStringIO import StringIO
            for filename in zip.namelist():
                if filename.startswith('__'): # do not process meta files
                    continue
                data = zip.read(filename)
                if len(data):
                    try:
                        # the following is taken from django.newforms.fields.ImageField:
                        #  load() is the only method that can spot a truncated JPEG,
                        #  but it cannot be called sanely after verify()
                        trial_image = Image.open(StringIO(data))
                        trial_image.load()
                        # verify() is the only method that can spot a corrupt PNG,
                        #  but it must be called immediately after the constructor
                        trial_image = Image.open(StringIO(data))
                        trial_image.verify()
                    except Exception:
                        # if a "bad" file is found we just skip it.
                        continue
                    while 1:
                        title = ' '.join([self.name, str(count)])
                        try:
                            p = Photo.objects.get(title=title)
                        except Photo.DoesNotExist:
                            photo = Photo(title=title, gallery=gallery)
                            photo.image.save(filename, ContentFile(data))
                            count = count + 1
                            break
                        count = count + 1
            zip.close()
            return gallery
