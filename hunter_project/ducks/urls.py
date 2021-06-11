from django.urls import path
from . import views
from django.urls import path
from .views import DuckList
from .views import DuckList, UsersDucks

urlpatterns = [
    path('ducks/', DuckList.as_view()),
    path('usersDucks/', UsersDucks.as_view()),
    path('usersDucks/<int:pk>', UsersDucks.as_view()),

]


