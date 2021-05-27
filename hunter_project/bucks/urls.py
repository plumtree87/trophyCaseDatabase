from django.urls import path
from . import views

urlpatterns = [
    path('bucks/', views.BuckList.as_view()),
]