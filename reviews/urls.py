from django.urls import path
from . import views
from .views import *



"""url paths"""
urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('add_review/', views.AddReview.as_view(), name='add_review'),
]
