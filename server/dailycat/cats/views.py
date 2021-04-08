# django_rest_framework -> RESTFul API
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import ListView

'''
## api schema
- GET /cats/ -> 사진 리스트 (/cats/?mypage=true)
- GET /cat/1/: title (투표수), 사진url, 좋아요 (is_like, 로그인상태일때에만)
- GET /cat/1/titles/ : 좋아요 (로그인상태일때만)
- GET /cat/1/titles/1/comments/

# - POST /cats/ -> 생성 (내부적으로 사용)

- PATCH /cat/1/titles/1/  -> title 좋아요
- PATCH /cat/1/ -> 고양이 좋아요 (user - cat)
- PATCH /cat/1/ -> 고양이 신고하기? (user - cat)
- POST /login/
'''

# from django.views import View
# # -> api
# # fbv (request) -> View -> TemplateView -> generics : ListView, DetailView, CreateView, UpdateView, DeleteView /
# # rest_framework
# # django fbv / View -> APIView -> generics: ListAPIView, DetailAPIView, CfeateAPIView ... / ViewSet

# class UserUpdateView(UpdateView):
#     model = User
#     fields = ['liked_cats', 'liked_titles']

#     def create(self, *args, **kwargs):
#         cats = self.liked_cats  # id
#         cats = Cats.is_not_reported.filter(id__in=cats).values_list('id', flat=True)
#         return super().create(*args, **kwargs)


# def title_like_view()
#     cat_id = requests.POST.get('cat_id')
#     user.liked_cat.add(cat_id)
#     user.save()
#     return 

# def cat_like_view()
#     cat_id = requests.POST.get('cat_id')
#     user.save_cat(cat_id)
#     return 

# cat CRUD

# api
# -> rest framework

# class CatViewSet(ModelViewSet):
#     model = Cat

# class TitleViewSet(ModelViewSet);
#     model = Title

# class ConmmentViewSet(ModelViewSet);
#     model = Comment
# url -> router /
# - list, detail, create, update, delete

# class CatListAPIView(ListAPIView):
#     model = Cat
#     fields = ['url', 'expose_date', 'pk']


# class CatListView(ListView):
#     model = Cat
#     template_name = 'my_name'


# class CatTemplateView(TemplateView):
#     template_name = 'my_name'

# # CatView.as_view()
# class CatView(View):
#     def get(request):
#         return render('tkslfd', context)
#     def post(request):
#         ...
#     def delete(reqest):
#         ...
#     # def post(reqest):


# def home(request):
#     return HttpResponse("hello world")
#     # return render('.html')

# def cat(request,cat_id):
#     # cat_id : pk (int)
#     # str, ...
#     # -> json()
#     return HttpResponse(f"This is a cat {cat_id}")

# # get, post, 
# def cat_list(request):
#     if request.METHOD == 'GET':
#     cats = Cat.objects.all()
#     # pagination = slkfnldfnn
#     return render('cat_list.hmtl', {'cats': cats})

# class CatListView(ListView):
#     model = Cat


# # list, detail, create(form), delete, update, login, logout
# # 
