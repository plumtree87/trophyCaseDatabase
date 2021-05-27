from django.urls import path
from . import views

urlpatterns = [
    path('reply/', views.ReplyList.as_view()),
]