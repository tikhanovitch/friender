from rest_framework import serializers
from django.contrib.auth.models import User
from booking_app.models import HotelOwner
# from booking_app.models import HotelOwner
from booking_app.models import Hobby


# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(required=False, max_length=30)
#     first_name = serializers.CharField(required=False, max_length=30)
#     last_name = serializers.CharField(required=False, max_length=30)
#     email = serializers.EmailField(required=False)
#
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", 'first_name', 'last_name', 'email']


class HotelOwnerSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, max_length=30)
    last_name = serializers.CharField(required=False, max_length=30)
    age = serializers.IntegerField(required=False)
    sex = serializers.CharField(required=False)

    def create(self, validated_data):
        return HotelOwner.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.save()
        return instance

#
# class HobbySerializer(serializers.Serializer):
#     name = serializers.CharField(required=False, max_length=30)
#     detail = serializers.CharField(required=False, max_length=50)
#
#     def create(self, validated_data):
#         return Hobby.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.detail = validated_data.get('detail', instance.detail)
#         instance.save()
#         return instance


# class HobbyModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hobby
#         fields = ["name", "detail"]


class HobbyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
