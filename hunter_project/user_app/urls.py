from django.conf.urls import url
from .views import UserRegistrationView, UserLoginView, UserProfileView, Email


urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view()),
    url(r'^profile', UserProfileView.as_view()),
    url('email', Email.as_view())
    ]