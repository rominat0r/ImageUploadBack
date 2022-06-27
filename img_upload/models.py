from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(
        _("Image"), upload_to=upload_to, blank=True, null=True)