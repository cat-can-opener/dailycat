from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .serializers import CatSerializer, TitleSerializer
from .models import Cat, Title


class CatViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    '''
    - list: GET /cats/
    - detail: GET /cats/<id>/
    - like, report: PATCH /cats/<pk>/
    '''
    http_method_names = ['get', 'patch']
    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    permission_classes = [IsAuthenticated]


class TitleViewSet(ListModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    '''
    - list: GET /cats/<cat_pk>/titles/
    - create: POST /cats/<cat_pk>/titles/
    - update: PATCH /cats/<cat_pk>/titles/<pk>/
    - delete: DELETE /cats/<cat_pk>/titles/<pk>/
    '''
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = TitleSerializer
