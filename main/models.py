from django.db import models


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


class Testimonial(models.Model):
    author = models.CharField(max_length=60)
    testimonial = models.TextField()
    occupation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.author


class Post(models.Model):
    title = models.CharField(max_length=255)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated_on = models.DateField(auto_now_add=False, auto_now=True)
    image = models.URLField()
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author
