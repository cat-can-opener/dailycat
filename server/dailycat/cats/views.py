from http import HTTPStatus

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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
        serilaizer = CatSerializer(Cat.objects.all(), many=True)
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

    def patch(self, request, pk):
        cat = self.get_object(pk)
        serializer = CatSerializer(
            cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(serializer.errors, status=400)


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
        serializer = TitleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        title = Title.objects.get(pk=pk)
        serializer = TitleSerializer(title, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        title = Title.objects.get(pk=pk)
        if title:
            title.delete()
            return Response("Delete Success", status=201)
        return Response(status=400)


class CommentView(APIView):
    '''
    LIST
    request: GET /comments/?title=<int>

    response:
    [
        {
            "id": <int>,
            "user": <int>,
            "title":<int>,
            "content": <str>,
        }
    ]
    '''

    def get(self, request):
        title_id = request.GET.get("title")
        comment = CommentSerializer(
            Comment.objects.filter(title=title_id), many=True)
        return Response(comment.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(
            comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        if comment:
            comment.delete()
            return Response("Delete Success", status=201)
        return Response(status=400)
