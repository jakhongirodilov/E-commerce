from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    img_url = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(User, blank=True, null=True, related_name="cart")


    def __str__(self) -> str:
        return f"{self.name}, Category :{self.category}, Owner: {self.owner}"
    