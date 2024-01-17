from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    password=models.IntegerField()
    phone=models.IntegerField()
    img=models.ImageField(upload_to='images',height_field=None,width_field=None,max_length=100)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name