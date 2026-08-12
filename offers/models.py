from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.CharField(max_length=50)
    image = models.ImageField(upload_to='offers/')

    def __str__(self):
        return self.title
