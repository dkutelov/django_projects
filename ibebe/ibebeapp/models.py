from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=200)
    buy_link = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name}'
