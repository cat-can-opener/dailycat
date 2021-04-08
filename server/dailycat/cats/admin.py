from django.contrib import admin
from . import models


@admin.register(models.Cat)
class CatAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Title)
class TitleAdmin(admin.ModelAdmin):
    pass



