from django.db import models

# Create your models here.


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()


class PopularCards(models.Model):
    title = models.TextField()
    description = models.TextField()
    imageUrl = models.ImageField(upload_to='images/')
