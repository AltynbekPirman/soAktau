from rest_framework import serializers

from main.serializers import LanguageSerializer
from news.models import News, Announcement, Question, Answer


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'text', 'created_date', 'photo_url')


class NewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'photo_url')


class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = ('id', 'title', 'text', 'created_date')


class AnnouncementListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = ('id', 'title')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('text', 'created_date')


class QuestionDetailSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, allow_null=True)

    class Meta:
        model = Question
        fields = ('question', 'created_date', 'answers', 'language')


class QuestionSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = Question
        fields = ('id', 'question', 'created_date', 'language')

