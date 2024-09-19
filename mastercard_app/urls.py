from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('faqs/', views.FAQList.as_view(), name='faq-list')
]
