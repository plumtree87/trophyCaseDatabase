from django.urls import path
from . import views
from django.urls import path
from .views import CommentList

urlpatterns = [
    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>', views.CommentList.as_view()),
]