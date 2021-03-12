from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)

    class CATEGORIES(models.TextChoices):
        mining = 'Mining',
        agriculture = 'Agriculture',
        infrastructure = 'Infrastructure',
        power = 'Power'

    category = models.CharField(
        max_length=20,
        choices=CATEGORIES.choices,
        default='Mining'
    )
    description = models.CharField(max_length=250)
    image_one = models.URLField()
    image_two = models.URLField(blank=True)
    image_three = models.URLField(blank=True)
    image_four = models.URLField(blank=True)
    project_url = models.URLField(blank=True)

    def __str__(self):
        return self.title