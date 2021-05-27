from django.urls import path
from . import views

urlpatterns = [
    path('ducks/', views.DuckList.as_view()),
]