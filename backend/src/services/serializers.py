from rest_framework import serializers
from services.models import Service, Post, SubService, Title


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'text', 'title', 'sub_service')


class PostTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'text')


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'title')


class SubServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubService
        fields = ('id', 'title')


class ServiceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'title')


class TitleSerializer(serializers.ModelSerializer):
    posts = PostTextSerializer(many=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'posts')


# class PostSerializer(serializers.ModelSerializer):
#     posts = PostTextSerializer(many=True)
#
#     class Meta:
#         model = Title
#         fields = ('name', 'posts')

