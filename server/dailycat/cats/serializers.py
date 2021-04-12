from rest_framework.serializers import ModelSerializer

from .models import Cat, Title


class CatSerializer(ModelSerializer):
    class Meta:
        model = Cat
        fields = (
            'id',
            'url',
            'created',
            'expose_date',
            'is_reported',
        )
        read_only_fields = (
            'id',
            'url',
            'created',
            'expose_date',
        )


class TitleSerializer(ModelSerializer):
    class Meta:
        model = Title
        fields = (
            'id',
            'content',
        )
        read_only_fields = ('id',)
