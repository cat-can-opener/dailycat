from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/",views.LoginView.as_view(),name="login"),
    path("signup/",views.SignupView.as_view(),name="signup"),
    path("mypage/",views.MypageView.as_view(),name="mypage")
]