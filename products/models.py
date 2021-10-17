from django.db import models
# from django.db.models.signals.pre_save 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
import random
import os
from .utils import unique_slug_generator
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext
def upload_image_path(instance,filename):
    new_filename = random.randint(1,3910209312)
    name,ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}{final_filename}'
#ModelQuerySet
class ProductQuerySet(models.query.QuerySet):
    # featured
    def featured(self):
        return self.filter(featured = True,active = True)
    # active
    def active(self):
        return self.filter(active = True)
#Model Manager 
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)
    def featured(self):
        return self.get_queryset().featured()
    def all(self):
        return self.get_queryset().active()
#Model
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=upload_image_path)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True,unique=True)
    objects = ProductManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    
@receiver(pre_save, sender=Product)
def _pre_save_receiver(sender, instance,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)