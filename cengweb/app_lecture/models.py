from django.db import models


class Lecture(models.Model):
    code = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
    )
    name = models.CharField(max_length=300)
    year_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    year = models.CharField(
        max_length=10,
        choices=year_choices,
        default='1'
    )
    term_choices = (
        ('Fall', 'Fall'),
        ('Spring', 'Spring'),
    )
    term = models.CharField(
        max_length=10,
        choices=term_choices,
        default='Fall'
    )

    image = models.ImageField(upload_to="uploads", blank=True)

    def __str__(self):
        return self.code + " " + self.name

