from django.urls import path
import rest_auth
from rest_auth.registration.views import VerifyEmailView
from .views import RegisterView, LoginView
app_name = "users"

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('signup/', RegisterView.as_view(), name='signup'),
    # path('logout/', rest_auth.views.LogoutView.as_view(), name='logout'),
    # path('account-confirm-email/',
    #      VerifyEmailView.as_view(), name='account_confirm_email'),
    # # path('signup', SignupView.as_view(), name='signup')
    # path('rest-auth/', include('rest_auth.urls')),
    # path('signup/', include('rest_auth.registration.urls'))
    # user/registration/ => 회원가입
    #username, password1,password2,email
    # user/login/ =>로그인
    # username,email,password
    # user/logout/
]
