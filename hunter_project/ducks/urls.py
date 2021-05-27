from django.urls import path
from . import views
from django.urls import path
from .views import DuckList
from . import views

urlpatterns = [
    path('ducks/', views.DuckList.as_view()),
]


