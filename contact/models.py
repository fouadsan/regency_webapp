from django.db import models
from django.contrib import admin


class Contact(models.Model):
    content = models.TextField()

    def __str__(self):
        return f"Contact"
