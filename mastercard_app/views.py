from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from mastercard_app.models import Faq
from mastercard_app.serializers import FAQSerializer


def members(request):
    return HttpResponse("Hello world!")


class FAQList(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FAQSerializer
