from django.urls import path
from . import views

urlpatterns = [
    path('bucks/', views.BuckList.as_view()),
    path('usersBucks/', views.UsersBucks.as_view()),
]