from django.db import models
from django.contrib.postgres.fields import ArrayField


class Poll(models.Model):
    question = models.CharField(max_length=250)
    answers = ArrayField(models.CharField(max_length=55, blank=False), size=2)

    def __str__(self):
        return self.question
