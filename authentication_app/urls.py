from django.urls import path
from .views import RegisterView, logout_session, login_session

urlpatterns = [
    path('', RegisterView.as_view(), name='Signup'),
    path('Login', login_session, name='Login'),
    path('Logout', logout_session, name='Logout'),
]
