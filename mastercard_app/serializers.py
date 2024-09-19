from rest_framework import serializers
from .models import Faq, PopularCards


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'question', 'answer']


class PopularCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularCards
        fields = ['id', 'title', 'description', 'imageUrl']

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['imageUrl'] = instance.image.url if instance.image else None
            return representation
