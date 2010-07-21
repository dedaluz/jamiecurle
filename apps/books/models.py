from django.db import models
from django.conf import settings
# Create your models here.

class Book(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    isbn = models.CharField(max_length=255, blank=True, null=True)
    photo = ImageWithThumbsField(upload_to='uploads/books/%Y/%m/%d', sizes=settings.PHOTO_SIZES)
