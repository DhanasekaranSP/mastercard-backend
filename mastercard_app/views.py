from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from mastercard_app.models import Faq, PopularCards
from mastercard_app.serializers import FAQSerializer, PopularCardsSerializer


def members(request):
    return HttpResponse("Hello world!")


class FAQList(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FAQSerializer


class PopularCardsListCreateAPIView(generics.ListCreateAPIView):
    queryset = PopularCards.objects.all()
    serializer_class = PopularCardsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        is_special = self.request.query_params.get('is_special', None)
        if is_special is not None:
            is_special = is_special.lower() == 'true'
            queryset = queryset.filter(is_special_card=is_special)
        return queryset


class PopularCardsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PopularCards.objects.all()
    serializer_class = PopularCardsSerializer
