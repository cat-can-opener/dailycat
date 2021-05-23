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
Cat
- [o] list: GET /cats/ -> 사진 리스트 (/cats/?mypage=true)
- [o] detail: GET /cat/1/: title (투표수), 사진url
- [o] update: PATCH /cat/1/ -> 고양이 좋아요
---
Title

- [o] list: GET /titles/?cat=1
- [o] create: POST /titles/
- [o] update: PATCH /titles/1/ -> <creator>
- [o] delete: DELETE /titles/1/

- [o] create: POST /titles/ -> login required
- [o] like: /titles/1/like/ -> <login required>
- [o] update: PATCH /titles/1/ -> login required -> <creator required>
- [o] delete: DELETE /titles/1/ -> login required -> <creator required>

---
# Comment

# - GET /comments/?title=1
# - POST /comments/
# - PATCH /comments/1/  -> 좋아요
# - DELETE /comments/1/
# - [ ] create : login required
# - [ ] update, delete: creator required

---

- signup
- login
# - [ ] mypage -> /cats?mypage=true

'''

urlpatterns = [
    # api router
    # path('', include(router.urls)),
    # path('', include(cats_router.urls)),
    path('cats/', CatListView.as_view(), name='cat_list'),
    path('cats/<int:pk>/', CatDetailView.as_view(), name='cat_detail'),
    path('cats/<int:pk>/like/', CatLikeView.as_view(), name='like_cat'),
    path('titles/', TitleView.as_view(), name='title_list'),
    path('titles/<int:pk>/', TitleView.as_view(), name='update_title'),
    path('titles/<int:pk>/like/', TitleLikeView.as_view(), name='like_title'),
    path('comments/', CommentView.as_view(), name='comment_list'),
    path('comments/<int:pk>/', CommentView.as_view(), name='update_comment'),
    path('comments/<int:pk>/', CommentView.as_view(), name='delete_comment'),
]
