from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    title_color = models.CharField(max_length=10, blank=True)
    border_color = models.CharField(max_length=10, blank=True)
    image_large = models.CharField(max_length=50, blank=True)
    image_small = models.CharField(max_length=50, blank=True)
    sub_headline = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    avatar_url = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    sub_title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=200)
    buy_link = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name}'
