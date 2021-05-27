from django.urls import path
from . import views
from django.urls import path
from .views import BassList
from . import views

urlpatterns = [
    path('fish/', views.BassList.as_view()),
]