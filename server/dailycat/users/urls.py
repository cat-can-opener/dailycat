from django.urls import path
import rest_auth
from rest_auth.registration.views import VerifyEmailView
from .views import RegisterView, LoginView
app_name = "users"

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('signup/', RegisterView.as_view(), name='signup'),
    # path('logout/', rest_auth.views.LogoutView.as_view(), name='logout'),

]
