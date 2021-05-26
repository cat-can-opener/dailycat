from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Cat, Title, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'title',
            'content'

        )
        read_only_fields = ('id',)


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = (
            'id',
            'user',
            'cat',
            'content',
            'liked_counts',
        )
        read_only_fields = ('id',)


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = (
            'id',
            'image',
            'created',
            'expose_date',
            'is_reported',
            # 'title_set',
        )
        read_only_fields = (
            'id',
            'image',
            'created',
            'expose_date',
        )


class CatDetailSerializer(serializers.ModelSerializer):
    # titles = TitleSerializer(many=True, source='title_set')
    titles_method = serializers.SerializerMethodField()

    class Meta:
        model = Cat
        fields = (
            'id',
            'image',
            'created',
            'expose_date',
            'is_reported',
            # 'title_set'
            # 'titles',
            'titles_method',
        )
        read_only_fields = (
            'id',
            'image',
            'created',
            'expose_date',
        )
        # depth = 2

    def get_titles_method(self, obj):
        titles = obj.title_set.all()[:3]
        return TitleSerializer(titles, many=True).data
