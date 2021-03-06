from rest_framework import serializers

from main.accessories import ImageLinker
from news.models import News, Announcement, Question


class NewsSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = News
        fields = ('kaz', 'rus')

    def get_icon_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.icon.url)

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            return self.context['request'].build_absolute_uri(obj.thumbnail.url)
        return None

    def group_by_lang_kaz(self, obj):
        return {
            'id': obj.id, 'title': obj.title_kaz, 'text': ImageLinker(obj.text_kaz).link_images(),
            'icon': self.get_icon_url(obj), 'createdAt': obj.created_date, 'isMain': obj.is_main,
            'viewCount': obj.view_count, 'thumbnail': self.get_thumbnail_url(obj)
        }

    def group_by_lang_rus(self, obj):
        return {
            'id': obj.id, 'title': ImageLinker(obj.title_rus).link_images(), 'text': obj.text_rus,
            'icon': self.get_icon_url(obj), 'createdAt': obj.created_date, 'isMain': obj.is_main,
            'viewCount': obj.view_count, 'thumbnail': self.get_thumbnail_url(obj)
        }


class AnnouncementSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Announcement
        fields = ('kaz', 'rus')

    def get_icon_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.icon.url)

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            return self.context['request'].build_absolute_uri(obj.thumbnail.url)
        return None

    def group_by_lang_kaz(self, obj):
        return {
            'id': obj.id, 'title': obj.title_kaz, 'text': obj.text_kaz,
            'icon': self.get_icon_url(obj), 'createdAt': obj.created_date, 'thumbnail': self.get_thumbnail_url(obj)
        }

    def group_by_lang_rus(self, obj):
        return {
            'id': obj.id, 'title': obj.title_rus,  'text': obj.text_rus,
            'icon': self.get_icon_url(obj), 'createdAt': obj.created_date, 'thumbnail': self.get_thumbnail_url(obj)
        }


class QuestionSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = Question
        fields = ('kaz', 'rus')

    @staticmethod
    def group_by_lang_kaz(obj):
        return {'id': obj.id, 'question': obj.question_kaz, 'answer': obj.answer_kaz, 'createdAt': obj.created_date}

    @staticmethod
    def group_by_lang_rus(obj):
        return {'id': obj.id, 'question': obj.question_rus, 'answer': obj.answer_rus, 'createdAt': obj.created_date}
