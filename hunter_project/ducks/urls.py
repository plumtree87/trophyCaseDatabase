from django.urls import path
from . import views
from django.urls import path
from .views import DuckList
from .views import DuckList

urlpatterns = [
    path('ducks/', DuckList.as_view()),
]


