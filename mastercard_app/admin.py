from django.contrib import admin

from mastercard_app.models import Faq, FilterCategory, PopularCards, SubCategories

# Register your models here.
admin.site.register(Faq)
admin.site.register(PopularCards)
admin.site.register(FilterCategory)
admin.site.register(SubCategories)
