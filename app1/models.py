from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone=models.CharField(max_length=100)
    start_desti=models.CharField(max_length=100)
    to_desti=models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name