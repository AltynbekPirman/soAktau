from rest_framework import serializers
from services.models import Service, Post, SubService, Title


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'text', 'title', 'sub_service')


class PostTextSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Post
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'text': obj.text_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'text': obj.text_rus}


class ServiceSerializer(serializers.ModelSerializer):
    # title = serializers.SerializerMethodField('group_by_lang')
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Service
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'id': obj.id, 'title': obj.title_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'id': obj.id, 'title': obj.title_rus}


class SubServiceSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = SubService
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'id': obj.id, 'title': obj.title_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'id': obj.id, 'title': obj.title_rus}


# class ServiceDetailSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Service
#         fields = ('id', 'title')


class TitleSerializer(serializers.ModelSerializer):
    # posts = PostTextSerializer(many=True)

    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Title
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'id': obj.id, 'title': obj.name_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'id': obj.id, 'title': obj.name_rus}


class TitleDetailSerializer(serializers.ModelSerializer):
    posts = PostTextSerializer(many=True)

    class Meta:
        model = Title
        fields = ('posts',)
