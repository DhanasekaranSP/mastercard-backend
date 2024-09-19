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


class PopularCardsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PopularCards.objects.all()
    serializer_class = PopularCardsSerializer
