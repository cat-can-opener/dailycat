from rest_framework import serializers
from http import HTTPStatus
from django.shortcuts import get_object_or_404
from .models import Cat, Title, Comment
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.generic import View
from django.core import serializers


class CatListSerializer(serializers.ModelSerializer):
    titles = serializers.SerializerMethodField('get_title')

    class Meta:
        model = Cat
        fields = ('id', 'url', 'titles')

    def get_title(self, obj):
        return obj.title_set.values_list('content', flat=True)[:3]


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = ('id', 'content', 'cat')


def cat_list(request):
    cats = Cat.objects.all()  # 'id', 'url', 'title' 3개

    data = []
    cat_data = Cat.objects.values('id', 'url')
    for cat in cat_data:
        cat_id = cat['id']
        title_data = Title.objects.filter(cat=cat_id).values_list('title')
        cat_data

    data = serializers.serialize("json", cats)
    return JsonResponse({"cat": data})


class ClassCatList(View):
    def get_context_data(self):
        return {'object_list': self.object_list}

    def get(self, request):
        self.object_list = Cat.objects.all()
        # filter
        # paginations
        conetextt = get_con

        return render('cat_list.html', context={'cats': cats})


class ClassCatList(ListView):
    model = Cat
    template_name = 'new.html'


# GET /cat/1/
# 좋아요, 신고하기 -> PATCH /cat/1/
# 진규님
class CatDetailView(View):
    # /cats/<pk>/
    def get(request, pk):
        cat = Cat.objects.get(pk=pk)
        cat_url = cat.url
        title = list(cat.title_set.values())
        if cat:
            return JsonResponse({"cat": cat_url, "title": title})
        return JsonResponse({"result": False})

    def patch(request):
        ...


def catdetail(request, pk):
    cat = Cat.objects.get(pk=pk)
    cat_url = cat.url
    title = list(cat.title_set.values())
    if cat:
        return JsonResponse({"cat": cat_url, "title": title})
    return JsonResponse({"result": False})


class TitleSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=255)


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('id', 'content',)


class TitleListView(ListAPIView):
    model = Title
    serializer_class = TitleSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        cat_id = request.GET.get('cat')
        queryset = queryset.objects.filter(cat=cat_id)
        return queryset

# View -> generics.ListView -> mixins
# GET /titles/


class TitleView(View):
    def get(self, request):
        cat_id = request.GET.get("cat")
        cat = Cat.objects.get(pk=cat_id)
        title = list(cat.title_set.values())
        return JsonResponse({"result": title})  # dictionary

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        cat_id = data['id']
        content = data['content']
        cat = Cat.objects.get(pk=cat_id)
        title = cat.title_set.create(
            content=content
        )
        return JsonResponse({"result": "Create Success"})

    def patch(self, request, pk):
        data = json.loads(request.body)
        cat_id = data['id']
        new_content = data['content']
        cat = Cat.objects.get(pk=cat_id)
        title = cat.title_set.get(pk=pk)
        title.content = new_content
        title.save()
        return JsonResponse({"result": "Update Success"})

    def delete(self, request, pk):
        data = json.loads(request.body)
        id = data['id']
        cat = Cat.objects.get(pk=id)
        title = cat.title_set.get(pk=pk)
        title.delete()
        return JsonResponse({"result": "Delete Success"})


class CommentView(View):
    def get(self, request):
        title_id = request.GET.get("title")
        title = Title.objects.get(pk=title_id)
        comment = list(title.comment_set.values())
        return JsonResponse({"result": comment})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        title_id = data['id']
        content = data['content']
        title = Title.objects.get(pk=title_id)
        comment = title.comment_set.create(
            content=content
        )
        return JsonResponse({"result": "Create Success"})

    def patch(self, request, pk):
        data = json.loads(request.body)
        title_id = data['id']
        new_content = data['content']
        title = Title.objects.get(pk=title_id)
        comment = title.comment_set.get(pk=pk)
        comment.content = new_content
        comment.save()
        return JsonResponse({"result": "Update Success"})

    def delete(self, request, pk):
        data = json.loads(request.body)
        id = data['id']
        title = Title.objects.get(pk=id)
        comment = title.comment_set.get(pk=pk)
        comment.delete()
        return JsonResponse({"result": "Delete Success"}, status_code=HTTPStatus.NO_CONTENT)


# -> api
# fbv (request) -> View -> TemplateView -> generics : ListView, DetailView, CreateView, UpdateView, DeleteView /
# rest_framework
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
