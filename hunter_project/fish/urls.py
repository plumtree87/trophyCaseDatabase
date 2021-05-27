from django.urls import path
from . import views

urlpatterns = [
    path('fish/', views.BassList.as_view()),
]