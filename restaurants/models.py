from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='restaurants/')

    def __str__(self):
        return self.name