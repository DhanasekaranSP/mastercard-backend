from django.db import models

# Create your models here.


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()


class PopularCards(models.Model):
    title = models.TextField()
    description = models.TextField()
    imageUrl = models.ImageField(upload_to='images/')
    is_special_card = models.BooleanField(default=False)
    ctaname = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.title


class FilterCategory(models.Model):
    parentname = models.CharField(max_length=255)

    def __str__(self):
        return self.parentname


class SubCategories(models.Model):
    childname = models.CharField(max_length=255)
    title = models.ForeignKey(
        FilterCategory, related_name='childitems', on_delete=models.CASCADE)

    def __str__(self):
        return self.childname
