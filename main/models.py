from django.db import models
from django.contrib import admin


class Section(models.Model):
    name = models.CharField(max_length=150, db_index=True, unique=True)
    description = models.TextField()
    image_one = models.ImageField(upload_to='images')  # Important!!!!!!
    image_two = models.ImageField(upload_to='images')  # Important!!!!!!
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at', )
        verbose_name = 'section'
        verbose_name_plural = 'sections'


class About(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    since = models.IntegerField()

    def __str__(self):
        return f"About"


class Project(models.Model):
    title = models.CharField(max_length=100)
    section = models.ForeignKey(
        Section, related_name='projects', on_delete=models.CASCADE)
    description = models.TextField()
    image_one = models.ImageField(upload_to='images')
    image_two = models.ImageField(blank=True, upload_to='images', null=True)
    image_three = models.ImageField(blank=True, upload_to='images', null=True)
    image_four = models.ImageField(blank=True, upload_to='images', null=True)
    project_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    occupation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    author = models.CharField(max_length=60)
    testimonial = models.TextField()
    occupation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.author


class ProjectCounter(models.Model):
    class CATEGORIES(models.TextChoices):
        mining = 'Mining',
        agriculture = 'Agriculture',
        infrastructure = 'Infrastructure',
        power = 'Power'

    category = models.CharField(
        max_length=20,
        choices=CATEGORIES.choices,
        default='Mining',
        unique=True,
    )
    number = models.IntegerField()

    def __str__(self):
        return f"{self.category} number"


class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
