from django.db import models

# Create your models here.

from django.db import models

class WebStyle(models.Model):
    bg_color = models.CharField(max_length=20, default="#ffffff")
    font_family = models.CharField(max_length=50, default="Arial, sans-serif")

    @classmethod
    def get_settings(cls):
        obj, created = cls.objects.get_or_create(id=1)
        return obj