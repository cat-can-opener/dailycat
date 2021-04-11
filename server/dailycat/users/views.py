from django.shortcuts import render, redirect
from django.views.generic import View,TemplateView
from django.contrib.auth import login
from .models import User

class LoginView(View):
    def get(self,request, *args, **kwargs):
        return render(
            request,
            "auth/login.html",
            {}
        )
    def post(self, request,*args,**kwargs):
        email = request.POST.get("email")
        if email:
            login(request,email)
            return redirect("")
        return redirect("users:login")

class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "auth/signup.html",
            {},
        )
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")

        user = User.objects.create(
            email=email,
        )

        user.save()

        return redirect("users/login")
        
class MypageView(TemplateView):
    template_name = "auth/mypage.html"
