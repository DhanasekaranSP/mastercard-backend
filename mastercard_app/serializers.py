from rest_framework import serializers
from .models import Faq, FilterCategory, PopularCards, SubCategories


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'question', 'answer']


class PopularCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularCards
        fields = ['id', 'title', 'description',
                  'imageUrl', 'ctaname', 'is_special_card']

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['imageUrl'] = instance.imageUrl.url if instance.imageUrl else None

            print(f"is_special_card: {instance.is_special_card}")

            if not instance.is_special_card:
                representation.pop('ctaname', None)

            return representation


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = ['id', 'childname']


class FilterCategorySerializer(serializers.ModelSerializer):
    childitems = ItemSerializer(many=True)

    class Meta:
        model = FilterCategory
        fields = ['id', 'parentname', 'childitems']
