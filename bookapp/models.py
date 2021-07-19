from django.db import models

# Create your models here.

class bookProduct(models.Model):
    bookName = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    version = models.CharField(max_length = 100)
    publishingYear = models.IntegerField()
    publisherName = models.CharField(max_length = 200)
    price = models.IntegerField()
    image = models.CharField(max_length = 5000)

    class Meta:
        verbose_name = 'book deteail'

