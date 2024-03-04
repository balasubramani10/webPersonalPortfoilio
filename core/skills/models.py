from django.db import models

# Create your models here.


class MyFrontEndSKills(models.Model):
    name = models.CharField(max_length = 64)
    icon = models.ImageField(upload_to="skills_icons")
    def __str__(self):
        return self.name

class MyBackEndSKills(models.Model):
    name = models.CharField(max_length = 64)
    icon = models.ImageField(upload_to="skills_icons")
    def __str__(self):
        return self.name
