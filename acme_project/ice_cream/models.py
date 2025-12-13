from django.db import models
from django.db.models import PositiveSmallIntegerField


class Wrapper(models.Model):
    title = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)


class Topping(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    is_published = models.BooleanField(default=True)


class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = PositiveSmallIntegerField(default=100)
    is_published = models.BooleanField(default=True)


class IceCream(models.Model):
    is_published = models.BooleanField(default=True)
    is_on_main = models.BooleanField(default=False)
    title = models.CharField(max_length=256)
    description = models.TextField()
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    toppings = models.ManyToManyField(
        Topping
    )
