from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as filters

from news.models import News, Announcement, Question
from news.serializers import NewsSerializer, AnnouncementSerializer, QuestionSerializer


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
    serializer_class = NewsSerializer
    ordering = ('-created_date', )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('is_main', )

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        if request.method == 'POST':
            self.news_id = request.data.get('id')
            try:
                self.news = News.objects.get(id=self.news_id)
            except News.DoesNotExist:
                raise ValidationError('api_error: Cannot find object with id {}'.format(self.news_id))

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        news = NewsSerializer(queryset, many=True, context={'request': request})
        kaz = [d['kaz'] for d in news.data]
        rus = [d['rus'] for d in news.data]
        return Response({'kaz': kaz, 'rus': rus})

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        news = get_object_or_404(queryset, pk=pk)
        serializer = NewsSerializer(news, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def counter(self, request, *args, **kwargs):
        if self.news:
            self.news.view_count += 1
            self.news.save(update_fields=['view_count'])
            return Response(status=200, data={'count': self.news.view_count})
        return Response(status=400, data={'id error': self.news_id})


class AnnouncementViewSet(GenericViewSet, ListModelMixin, ):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    ordering = ('-created_date', )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        titles = AnnouncementSerializer(queryset, many=True, context={'request': request})
        kaz = [d['kaz'] for d in titles.data]
        rus = [d['rus'] for d in titles.data]
        return Response({'kaz': kaz, 'rus': rus})

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        announcement = get_object_or_404(queryset, pk=pk)
        serializer = AnnouncementSerializer(announcement, context={'request': request})
        return Response(serializer.data)


class QuestionViewSet(GenericViewSet, ListModelMixin, CreateModelMixin,):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        services = QuestionSerializer(queryset, many=True)
        kaz = [d['kaz'] for d in services.data]
        rus = [d['rus'] for d in services.data]
        return Response({'kaz': kaz, 'rus': rus})

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        question = QuestionSerializer(question)
        return Response(question.data)