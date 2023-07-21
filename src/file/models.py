import uuid, datetime
from django.db import models
from django.db import models
from io import BytesIO
from PIL import Image


def compress(image):
    from django.core.files import File
    
    im = Image.open(image)
    im_io = BytesIO() 
    im.thumbnail(size=(500, 500)) 
    im.save(im_io, 'JPEG')
    new_image = File(im_io, name=image.name)
    return new_image


def upload(instance, filename):
    today = datetime.datetime.now()
    file_format = filename.split('.')[-1]
    return f"{today.year}/{today.month}/{today.day}/{uuid.uuid4()}.{file_format}"


class File(models.Model):
    image = models.ImageField(upload_to=upload)
    format = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    ordering = models.IntegerField(default=1)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs):
        compressed_image = compress(self.image)
        self.image = compressed_image
        self.format = self.image.name.split('.')[-1]
        self.name = self.image.name if not self.name else self.name
        return super(File, self).save(*args, **kwargs)
