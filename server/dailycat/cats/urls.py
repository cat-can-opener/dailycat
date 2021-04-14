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
    path('catss/',cat_list,name = 'cat_list'),
    path('cat/<int:pk>/',catdetail,name='detail'),
    path('titles/',TitleView.as_view(), name='create_title'),
    path('titles/<int:pk>/',TitleView.as_view(), name='update_title'),
    path('titles/<int:pk>/',TitleView.as_view(), name='delete_title'),
    path('comments/',CommentView.as_view(), name='commentlist_list'),
    path('comments/<int:pk>/',CommentView.as_view(), name='update_comment'),
    path('comments/<int:pk>/',CommentView.as_view(), name='delete_comment'),

]
