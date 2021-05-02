from django.urls import path, include
from rest_framework_nested import routers

from .views import *
from .api_views import CatViewSet, TitleViewSet


app_name = 'cat'

# router = routers.SimpleRouter()
# router.register('cats', CatViewSet, basename='cat')

# cats_router = routers.NestedSimpleRouter(router, r'cats', lookup='cat')
# cats_router.register(r'titles', TitleViewSet, basename='title')

'''
- list: GET /cats/ -> 사진 리스트 (/cats/?mypage=true)
- detail: GET /cat/1/: title (투표수), 사진url
- update: PATCH /cat/1/ -> 고양이 좋아요, 신고하기?

---

- GET /titles/?cat=1
- POST /titles/
- PATCH /titles/1/
- DELETE /titles/1/
- PATCH /titles/1/  -> title 좋아요

---

- GET /comments/?title=1
- POST /comments/
- PATCH /comments/1/  -> 좋아요
- DELETE /comments/1/

---
'''

urlpatterns = [
    # api router
    # path('', include(router.urls)),
    # path('', include(cats_router.urls)),
    path('cats/', cat_list, name='cat_list'),
    path('cat/<int:pk>/', catdetail, name='detail'),
    path('titles/', TitleView.as_view(), name='create_title'),
    path('titles/<int:pk>/', TitleView.as_view(), name='update_title'),
    path('titles/<int:pk>/', TitleView.as_view(), name='delete_title'),
    path('comments/', CommentView.as_view(), name='commentlist_list'),
    path('comments/<int:pk>/', CommentView.as_view(), name='update_comment'),
    path('comments/<int:pk>/', CommentView.as_view(), name='delete_comment'),
]
