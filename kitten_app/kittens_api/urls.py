from django.urls import path
from .views import (
    BreedListView, KittenListView, KittenDetailView, KittenCreateView,
    KittenUpdateView, KittenDeleteView, KittenRatingView
)

urlpatterns = [
    path('breeds/', BreedListView.as_view(), name='breed-list'),
    path('kittens/', KittenListView.as_view(), name='kitten-list'),
    path('kittens/<int:pk>/', KittenDetailView.as_view(), name='kitten-detail'),
    path('kittens/add/', KittenCreateView.as_view(), name='kitten-add'),
    path('kittens/<int:pk>/edit/', KittenUpdateView.as_view(), name='kitten-update'),
    path('kittens/<int:pk>/delete/', KittenDeleteView.as_view(), name='kitten-delete'),
    path('kittens/<int:pk>/rate/', KittenRatingView.as_view(), name='kitten-rate'),
]
