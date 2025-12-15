from django.db import models
from django.db.models import PositiveSmallIntegerField
from core.models import PublishedModel


class Wrapper(PublishedModel, models.Model):
    title = models.CharField(max_length=256)


class Topping(PublishedModel, models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)


class Category(PublishedModel, models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = PositiveSmallIntegerField(default=100)


class IceCream(PublishedModel, models.Model):
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
