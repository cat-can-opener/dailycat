from django.urls import path, include
from rest_framework_nested import routers

from .views import *
from .api_views import CatViewSet, TitleViewSet


app_name = 'cat'

router = routers.SimpleRouter()
router.register('cats', CatViewSet, basename='cat')

cats_router = routers.NestedSimpleRouter(router, r'cats', lookup='cat')
cats_router.register(r'titles', TitleViewSet, basename='title')


urlpatterns = [
    # api router
    path('', include(router.urls)),
    path('', include(cats_router.urls)),

#     path('',CatListView.as_view(),name = 'home'),
#     path('cats/',CatListView.as_view(),name = 'home'),
#     path('cat/<int:pk>/',CatDetailView.as_view(),name='detail'),
#     path('cat/<int:pk>/titles/',TitleView.as_view(),name='title'),
#     path('cat/<int:pk>/titles/<int:id>/comments',CommentView.as_view(),name='comment'),
#     path('cat/new',new ,name='new'),
#     path('cat/create',CatCreateView.as_view() ,name='new')
] 
