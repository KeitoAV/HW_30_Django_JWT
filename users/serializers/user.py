
from rest_framework import serializers

from users.models import User, Location


class UserListSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField(required=True)
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True,
    )

    class Meta:
        model = User
        exclude = ['password']


class UserDetailSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField(required=True)
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True,
    )

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location = serializers.SlugRelatedField(
        required=False,
        slug_field='name',
        many=True,
        queryset=Location.objects.all(),
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('location', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(user.password)  # hash password
        user.save()

        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.location.add(location_obj)

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        slug_field='name',
        many=True,
        queryset=Location.objects.all(),
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        if self._locations:
            user.location.clear()
            for location in self._locations:
                location_obj, _ = Location.objects.get_or_create(name=location)
                user.location.add(location_obj)

        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
