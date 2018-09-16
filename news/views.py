from django.shortcuts import render, get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as filters

from main.models import Language
from news.models import News, Announcement, Question
from news.serializers import NewsSerializer, AnnouncementSerializer, NewsListSerializer, AnnouncementListSerializer, \
    QuestionSerializer, QuestionDetailSerializer


def get_language_filter(_model_):

    class IntermediateLanguageFilter(filters.FilterSet):
        lang = filters.CharFilter(field_name="language__code")

        class Meta:
            model = _model_
            fields = ('lang',)

    return IntermediateLanguageFilter


NewsFilter = get_language_filter(News)
AnnouncementFilter = get_language_filter(Announcement)
QuestionFilter = get_language_filter(Question)


class NewsViewSet(GenericViewSet, ListModelMixin, ):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    ordering = ('-created_date', )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = NewsFilter

    def retrieve(self, request, pk=None):
        queryset = News.objects.all()
        news = get_object_or_404(queryset, pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)


class AnnouncementViewSet(GenericViewSet, ListModelMixin, ):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementListSerializer
    ordering = ('-created_date', )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = AnnouncementFilter

    def retrieve(self, request, pk=None):
        queryset = Announcement.objects.all()
        announcement = get_object_or_404(queryset, pk=pk)
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)


class QuestionViewSet(GenericViewSet, ListModelMixin, CreateModelMixin,):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    ordering = ('-created_date', )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = QuestionFilter

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.lang = Language.objects.get(code=self.kwargs.get('lang_code'))

    def list(self, request, *args, **kwargs):
        lang = Language.objects.get(code=self.kwargs.get('lang_code'))
        queryset = Question.objects.filter(language=lang)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, lang_code=None):
        queryset = Question.objects.filter(language=self.lang)
        question = get_object_or_404(queryset, pk=pk)
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        lang = Language.objects.get(code=self.kwargs.get('lang_code'))
        Question.objects.create(language=lang, question=request.data.get('question'))
        return Response(status=201, data={'status': 'Everything was ok, Bro'})