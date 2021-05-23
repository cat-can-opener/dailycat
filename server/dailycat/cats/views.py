from http import HTTPStatus
from distutils.util import strtobool

from rest_framework import serializers, permissions, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Cat, Title, Comment
from .serializers import CatSerializer, CatDetailSerializer, TitleSerializer, CommentSerializer


def validate_like(like: str) -> bool:
    '''
    true, True, false 등의 스트링을 python boolean으로 변환

    다른 값이 들어오면 rasise ValidationError
    '''
    try:
        return bool(strtobool(like))  # true, True, on, y, yes
    except (ValueError, AttributeError):
        raise exceptions.ValidationError(
            detail='data required: "like" should be "true" or "false"')


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


class CatLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        like = request.POST.get('like')
        is_like = validate_like(like)

        cat = get_object_or_404(Cat, pk=pk)
        if is_like:
            request.user.liked_cats.add(cat)
        else:
            request.user.liked_cats.remove(cat)
        return Response(status=200)


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # READ: AllowAny
    # WRITE: post, patch, delete: IsAuthenticated -> 401
    # perssmission -> AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly ...

    def get(self, request):
        cat_id = request.GET.get("cat")
        title = TitleSerializer(Title.objects.filter(cat=cat_id), many=True)
        return Response(title.data)

    def post(self, request, *args, **kwargs):
        '''create title: login required'''
        # TODO: add login required
        serializer = TitleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        title = get_object_or_404(Title, pk=pk)

        if request.user != title.user:
            raise exceptions.PermissionDenied(
                detail="다른 유저의 title은 수정할 수 없습니다")

        serializer = TitleSerializer(title, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        title = get_object_or_404(Title, pk=pk)

        if request.user != title.user:
            raise exceptions.PermissionDenied(
                detail="다른 유저의 title은 수정할 수 없습니다")

        title.delete()
        return Response("Delete Success", status=204)


class TitleLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        is_like: bool = validate_like(request.POST.get('like'))

        title = get_object_or_404(Title, pk=pk)
        if is_like:
            request.user.liked_titles.add(title)
        else:
            request.user.liked_titles.remove(title)

        return Response(status=200)


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
