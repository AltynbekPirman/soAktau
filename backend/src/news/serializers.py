from rest_framework import serializers

from main.serializers import LanguageSerializer
from news.models import News, Announcement, Question


class NewsSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = News
        fields = ('kaz', 'rus')

    def get_thumbnail_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.icon.url)

    def group_by_lang_kaz(self, obj):
        return {'id': obj.id, 'title': obj.title_kaz, 'text': obj.text_kaz, 'icon': self.get_thumbnail_url(obj)}

    def group_by_lang_rus(self, obj):
        return {'id': obj.id, 'title': obj.title_rus, 'text': obj.text_rus, 'icon': self.get_thumbnail_url(obj)}


class AnnouncementSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Announcement
        fields = ('kaz', 'rus')

    def get_thumbnail_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.icon.url)

    def group_by_lang_kaz(self, obj):
        return {'id': obj.id, 'title': obj.title_kaz, 'text': obj.text_kaz, 'icon': self.get_thumbnail_url(obj)}

    def group_by_lang_rus(self, obj):
        return {'id': obj.id, 'title': obj.title_rus,  'text': obj.text_rus, 'icon': self.get_thumbnail_url(obj)}


class QuestionSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Question
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'id': obj.id, 'question': obj.question_kaz, 'answer': obj.answer_kaz}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'id': obj.id, 'question': obj.question_rus, 'answer': obj.answer_rus}
