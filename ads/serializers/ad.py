from rest_framework import serializers
from ads.models.ad import Ad
from users.models import User
from users.validators import check_is_published_status


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class AdListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Ad
        exclude = ['is_published', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    is_published = serializers.BooleanField(validators=[check_is_published_status])

    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        fields = '__all__'


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']
