from django.core.validators import URLValidator
from django.db import models


class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, primary_key=True)
    office_code = models.CharField(max_length=20)
    e_mail = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=15)
    web_site = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.name + " " + self.surname
