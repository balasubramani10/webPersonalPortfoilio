from django.db import models

# Create your models here.


class MyProjects(models.Model):
    title = models.CharField(max_length = 64)
    image = models.ImageField(upload_to="project_images")
    github_link = models.CharField(max_length = 512)
    live_link = models.CharField(max_length = 512)
    def __str__(self):
        return self.title