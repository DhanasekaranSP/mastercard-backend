from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('faqs/', views.FAQList.as_view(), name='faq-list'),
    path('popular-cards/', views.PopularCardsListCreateAPIView.as_view(),
         name='popular-cards-list-create'),
    path('popular-cards/<int:pk>/',
         views.PopularCardsDetailAPIView.as_view(), name='popular-cards-detail'),

    path('filter-categories/',
         views.FilterCategoryListView.as_view(), name='title-list'),

    path('offering-cards/', views.OfferingCardListCreateAPIView.as_view(),
         name='offering-cards-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
