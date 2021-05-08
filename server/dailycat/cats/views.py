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
from .serializers import CatSerializer, CatDetailSerializer, TitleSerializer, CommentSerializer


class CatListView(APIView):
    '''
    response:
    # localhost:8000/swagger
    [
        {
            'id': <int>,
            'url': <str>,
            'created': <str>,
            'exposed_date': <str>,
            'is_reported': <bool>
        },
        ...
    ]
    '''

    def get(self, request):
        serilaizer = CatListSerializer(Cat.objects.all(), many=True)
        return Response(serilaizer.data)


class CatDetailView(APIView):
    '''
    response:
    # localhost:8000/swagger
    [
        {
            'id': <int>,
            'url': <str>,
            'created': <str>,
            'exposed_date': <str>,
            'is_reported': <bool>
            # display 3 titles
            'titles': [
                'user': {
                    'id': <int>,
                    'name': <str>,
                }
                'id': <int>,
                'content': <str>,
                'created': <str>,
                'liked_counts': <int>,
                'cat': <int>,
            ]
        },
        ...
    ]
    '''

    def get_object(self, pk):
        return get_object_or_404(Cat, pk=pk)

    def get(self, request, pk):
        cat = self.get_object(pk)
        serializer = CatDetailSerializer(cat)
        return Response(serializer.data)


class TitleView(APIView):
    '''
    LIST
    request: GET /titles/?cat=<int>

    response:
    [
        {
            "user": <int>,
            "id": <int>,
            "content": <str>,
            "liked_counts": <int>,
        }
    ]
    '''

    def get(self, request):
        cat_id = request.GET.get("cat")
        title = TitleSerializer(Title.objects.filter(cat=cat_id), many=True)
        return Response(title.data)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        title = TitleSerializer(data=request.data)
        if not title.is_valid():
            return Response("")
        title.save()
        return Response(
            status_code=HTTPStatus.CREATED,
            data=TitleSerializer(title).data,
        )
        # cat_id = data['id']
        # content = data['content']
        # cat = Cat.objects.get(pk=cat_id)
        # title = Title.objects.create(
        #     content=content
        # )
        # RESTFul api
        # create -> 201 CREATED
        # {'id': 2, 'content': 'test'}
        # return Response(
        #     status_code=HTTPStatus.CREATED,
        #     data=TitleSerializer(title).data,
        # )

    def patch(self, request, pk):
        data = json.loads(request.body)
        cat_id = data['id']
        new_content = data['content']
        cat = Cat.objects.get(pk=cat_id)
        title = cat.title_set.get(pk=pk)
        title.content = new_content
        title.save()
        return Response("Update Success")

    def delete(self, request, pk):
        data = json.loads(request.body)
        id = data['id']
        cat = Cat.objects.get(pk=id)
        title = cat.title_set.get(pk=pk)
        title.delete()
        return Response("Delete Success")


class CommentView(APIView):
    def get(self, request):
        title_id = request.GET.get("title")
        comment = CommentSerializer(
            Comment.objects.filter(title=title_id), many=True)
        return Response(comment.data)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        title_id = data['id']
        content = data['content']
        title = Title.objects.get(pk=title_id)
        comment = title.comment_set.create(
            content=content
        )
        return Response("Create Success")

    def patch(self, request, pk):
        data = json.loads(request.body)
        title_id = data['id']
        new_content = data['content']
        title = Title.objects.get(pk=title_id)
        comment = title.comment_set.get(pk=pk)
        comment.content = new_content
        comment.save()
        return Response("Update Success")

    def delete(self, request, pk):
        data = json.loads(request.body)
        id = data['id']
        title = Title.objects.get(pk=id)
        comment = title.comment_set.get(pk=pk)
        comment.delete()
        return Response("Delete Success")
