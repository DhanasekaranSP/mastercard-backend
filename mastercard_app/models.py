from django.db import models

# Create your models here.


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
