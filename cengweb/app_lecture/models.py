from django.db import models
from app_lecturer.models import Lecturer
from app_lab.models import Lab


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

    secme_choises = (
        ('Seçmeli', 'Seçmeli'),
        ('Zorunlu', 'Zorunlu'),
    )

    kredi = models.CharField(max_length=3, blank=True, null=True, default="0")
    secme = models.CharField(max_length=20,choices=secme_choises, blank=True, null=True)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, blank=True, null=True)
    lab = models.ForeignKey(Lab, blank=True, null=True)
    aciklama = models.TextField()

    def __str__(self):
        return self.code + " " + self.name


class Question(models.Model):
    name = models.CharField(max_length=150, blank=True)
    question = models.TextField(blank=True)
    mail = models.EmailField(blank=True)

    def __str__(self):
        return self.question + " " + self.mail

