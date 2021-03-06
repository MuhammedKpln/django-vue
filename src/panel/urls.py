from django.urls import path
from .views import LoginView, RegisterView, LogoutView, IndexView, Dashboard

urlpatterns = [
    path('', IndexView.as_view(), name="Index"),
    path('panel/', Dashboard.as_view(), name="Dashboard"),
    path('login', LoginView.as_view(), name="Login"),
    path('register', RegisterView.as_view(), name="Register"),
    path('logout', LogoutView, name="Logout"),
]
