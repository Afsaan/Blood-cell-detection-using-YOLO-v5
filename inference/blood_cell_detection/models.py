from django.db import models

# Create your models here.
class File_Upload(models.Model):
    file = models.FileField()
