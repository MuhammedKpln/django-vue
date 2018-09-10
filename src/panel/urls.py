from django.urls import path
from .views import LoginView, RegisterView, LogoutView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="PanelHomePage"),
    path('login', LoginView.as_view(), name="Login"),
    path('register', RegisterView.as_view(), name="Register"),
    path('logout', LogoutView, name="Logout"),
]
