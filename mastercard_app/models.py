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


class OfferingCard(models.Model):
    cardName = models.CharField(max_length=255)
    cardImageUrl = models.ImageField(upload_to='offering_cards/')
    applyNowUrl = models.URLField()
    rateFeesUrl = models.URLField()
    cardheadLine = models.CharField(max_length=255)
    cardDescription = models.TextField()
    annualFees = models.DecimalField(max_digits=10, decimal_places=2)
    specialFees = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    # Issuer Id corresponds to SubCategories' childname under parentname 'issuers'
    issuer = models.ForeignKey(SubCategories, on_delete=models.CASCADE)

    # Many-to-many relationship to track categories (parent-child) of the card
    categoryList = models.ManyToManyField(
        SubCategories, related_name='offering_cards')

    def __str__(self):
        return self.cardName
