from django.urls import path
from . import views

app_name = "cat"
urlpatterns = [
    path("",views.CatListView.as_view(),name = "home"),
    path("cats/",views.CatListView.as_view(),name = "home"),
    path("cat/<int:pk>/",views.CatDetailView.as_view(),name="detail"),
    path("cat/<int:pk>/titles/",views.TitleView.as_view(),name="title"),
    path("cat/<int:pk>/titles/<int:id>/comments",views.CommentView.as_view(),name="comment")
] 