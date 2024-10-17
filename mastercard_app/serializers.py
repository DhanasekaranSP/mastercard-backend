from rest_framework import serializers
from .models import Faq, FilterCategory, OfferingCard, PopularCards, SubCategories


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


class OfferingCardSerializer(serializers.ModelSerializer):
    issuer = ItemSerializer()
    categoryList = ItemSerializer(many=True)

    class Meta:
        model = OfferingCard
        fields = ['id', 'cardName', 'cardImageUrl', 'applyNowUrl', 'rateFeesUrl',
                  'cardheadLine', 'cardDescription', 'annualFees', 'specialFees',
                  'issuer', 'categoryList']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Ensuring cardImageUrl is returned as a full URL
        request = self.context.get('request')
        if instance.cardImageUrl:
            card_image_url = instance.cardImageUrl.url
            # If request is present, include the full URL
            if request is not None:
                card_image_url = request.build_absolute_uri(card_image_url)
            representation['cardImageUrl'] = card_image_url
        else:
            representation['cardImageUrl'] = None

        return representation
