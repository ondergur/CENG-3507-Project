from django.db import models


class Comment(models.Model):
    subject = models.CharField(max_length=150, blank=True)
    comment = models.TextField(blank=True)
    mail = models.EmailField(blank=True)

    def __str__(self):
        return self.subject + " " + self.mail