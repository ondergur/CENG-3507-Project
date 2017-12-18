from django.db import models


class Lab(models.Model):
    code = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
    )
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    aciklama = models.TextField()

    def __str__(self):
        return self.code + " " + self.name
