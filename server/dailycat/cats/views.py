import json
from http import HTTPStatus

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView
from django.core import serializers

from .models import Cat, Title, Comment


@api_view(('GET',))
def cat_list(request):
    cats = Cat.objects.values('id', 'url')

    # cats:
    return Response(data=cats)


# GET /cat/1/
# 좋아요, 신고하기 -> PATCH /cat/1/
# 진규님
class CatDetailView(APIView):
    # /cats/<pk>/
    def get(request, pk):
        cat = Cat.objects.get(pk=pk)
        cat_url = cat.url
        title = list(cat.title_set.values())
        if cat:
            return JsonResponse({"cat": cat_url, "title": title})
        return JsonResponse({"result": False})

    def patch(request):
        ...


def catdetail(request, pk):
    cat = Cat.objects.get(pk=pk)
    cat_url = cat.url
    title = list(cat.title_set.values())
    if cat:
        return JsonResponse({"cat": cat_url, "title": title})
    return JsonResponse({"result": False})


class TitleView(APIView):
    def get(self, request):
        cat_id = request.GET.get("cat")
        cat = Cat.objects.get(pk=cat_id)
        title = list(cat.title_set.values())
        return JsonResponse({"result": title})  # dictionary

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        cat_id = data['id']
        content = data['content']
        cat = Cat.objects.get(pk=cat_id)
        title = cat.title_set.create(
            content=content
        )
        return JsonResponse({"result": "Create Success"})

    def patch(self, request, pk):
        data = json.loads(request.body)
        cat_id = data['id']
        new_content = data['content']
        cat = Cat.objects.get(pk=cat_id)
        title = cat.title_set.get(pk=pk)
        title.content = new_content
        title.save()
        return JsonResponse({"result": "Update Success"})

    def delete(self, request, pk):
        data = json.loads(request.body)
        id = data['id']
        cat = Cat.objects.get(pk=id)
        title = cat.title_set.get(pk=pk)
        title.delete()
        return JsonResponse({"result": "Delete Success"})


class CommentView(APIView):
    def get(self, request):
        title_id = request.GET.get("title")
        title = Title.objects.get(pk=title_id)
        comment = list(title.comment_set.values())
        return JsonResponse({"result": comment})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        title_id = data['id']
        content = data['content']
        title = Title.objects.get(pk=title_id)
        comment = title.comment_set.create(
            content=content
        )
        return JsonResponse({"result": "Create Success"})

    def patch(self, request, pk):
        data = json.loads(request.body)
        title_id = data['id']
        new_content = data['content']
        title = Title.objects.get(pk=title_id)
        comment = title.comment_set.get(pk=pk)
        comment.content = new_content
        comment.save()
        return JsonResponse({"result": "Update Success"})

    def delete(self, request, pk):
        data = json.loads(request.body)
        id = data['id']
        title = Title.objects.get(pk=id)
        comment = title.comment_set.get(pk=pk)
        comment.delete()
        return JsonResponse({"result": "Delete Success"}, status_code=HTTPStatus.NO_CONTENT)
