from django.urls import path
from .views import *

app_name = "cat"
urlpatterns = [
    path("",CatListView.as_view(),name = "home"),
    path("cats/",CatListView.as_view(),name = "home"),
    path("cat/<int:pk>/",CatDetailView.as_view(),name="detail"),
    path("cat/<int:pk>/titles/",TitleView.as_view(),name="title"),
    path("cat/<int:pk>/titles/<int:id>/comments",CommentView.as_view(),name="comment"),
    path("cat/new",new ,name="new"),
    path("cat/create",CatCreateView.as_view() ,name="new")
] 