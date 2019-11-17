from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name