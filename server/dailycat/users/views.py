from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth import login
from django.contrib import auth
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"login": True})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user_id = data['id']
        password = data['password']
        print(user_id)
        print(password)

        user = auth.authenticate(
            request, email="test@naver.com", password=12345)
        print(user)
        if user:
            auth.login(request, user)
            return JsonResponse({"result": True})
        else:
            return JsonResponse({"result": False})


@method_decorator(csrf_exempt, name="dispatch")
class SignupView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"signup": True})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user_id = data['id']
        password = data['password']
        user = User.objects.create(
            email=user_id, password=password
        )

        return JsonResponse({"result": True})


def logout(request):
    auth.logout(request)
    return redirect('/')
