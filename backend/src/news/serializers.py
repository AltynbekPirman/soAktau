from rest_framework import serializers

from main.serializers import LanguageSerializer
from news.models import News, Announcement, Question


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'text', 'created_date', 'photo_url')


class NewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'photo_url')


class AnnouncementSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Announcement
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'id': obj.id, 'title': obj.title_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'id': obj.id, 'title': obj.title_rus}


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Announcement
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'text': obj.text_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'text': obj.text_rus}


class QuestionSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = Question
        fields = ('id', 'question', 'created_date', 'language')

