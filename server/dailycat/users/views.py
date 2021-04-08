from models import User
from django.views.generic import UpdateView
from . import forms
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ['liked_cats', 'liked_titles']

#     def create(self, *args, **kwargs):
#         cats = self.liked_cats  # id
#         cats = Cats.is_not_reported.filter(id__in=cats).values_list('id', flat=True)
#         return super().create(*args, **kwargs)
