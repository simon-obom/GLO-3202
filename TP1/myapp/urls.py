from django.urls import path
from .views import get_users, register_user, login_user, logout_user, loggedin_view

urlpatterns = [
    path("api/users/", get_users, name="get_users"),
    path("api/register/", register_user, name="register_user"),
    path("api/login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("loggedin/", loggedin_view, name="loggedin"),
]
