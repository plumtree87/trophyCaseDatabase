from django.urls import path
from . import views
from django.urls import path
from .views import ReplyList
from . import views

urlpatterns = [
    path('reply/', views.ReplyList.as_view()),
]