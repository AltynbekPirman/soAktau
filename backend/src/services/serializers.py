from rest_framework import serializers
from services.models import Service, Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'text', 'title', 'sub_service')


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'title')


class ServiceDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = Service
        fields = ('id', 'title', 'posts')
