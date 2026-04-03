from django.db import models

class WebStyle(models.Model):
    bg_color = models.CharField(max_length=20, default="#f3f4f6") 
    
    text_color = models.CharField(max_length=20, default="#1f2937")

    secondary_color = models.CharField(max_length=20, default="#4f46e5")

    btn_text_color = models.CharField(max_length=20, default="#ffffff")
    
    font_family = models.CharField(max_length=255, default="ui-sans-serif, system-ui, sans-serif")

    @classmethod
    def get_settings(cls):
        obj, created = cls.objects.get_or_create(id=1)
        return obj