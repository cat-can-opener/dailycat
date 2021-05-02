from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    # path('login', LoginView.as_view(), name='login'),
    # path('signup', SignupView.as_view(), name='signup')

    # user/registration/ => 회원가입
    #username, password1,password2,email
    # user/login/ =>로그인
    # username,email,password
    # user/logout/
]
