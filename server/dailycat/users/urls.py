from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignupView.as_view(), name='signup')

]
