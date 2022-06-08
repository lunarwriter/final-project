from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta():
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=260)
    webname = models.CharField(max_length=260, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friend_name(self):
        return self.webname


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=260)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
