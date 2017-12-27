from django.db import models


class Lab(models.Model):
    code = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
    )
    name = models.CharField(max_length=300)
    capacity = models.CharField(max_length=20)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    explanation = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.code + " " + self.name
