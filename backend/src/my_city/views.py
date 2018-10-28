from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from my_city.models import CityNews
from my_city.serializers import CityNewsSerializer


class CityNewsViewSet(GenericViewSet, ListModelMixin, ):
    queryset = CityNews.objects.all()
    serializer_class = CityNewsSerializer
    ordering = ('-created_date', )

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        if request.method == 'POST':
            self.city_news_id = request.data.get('id')
            try:
                self.city_news = CityNews.objects.get(id=self.city_news_id)
            except CityNews.DoesNotExist:
                raise ValidationError('api_error: Cannot find object with id {}'.format(self.city_news_id))

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        news = CityNewsSerializer(queryset, many=True, context={'request': request})
        kaz = [d['kaz'] for d in news.data]
        rus = [d['rus'] for d in news.data]
        return Response({'kaz': kaz, 'rus': rus})

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        news = get_object_or_404(queryset, pk=pk)
        serializer = CityNewsSerializer(news, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def counter(self, request, *args, **kwargs):
        if self.city_news:
            self.city_news.view_count += 1
            self.city_news.save(update_fields=['view_count'])
            return Response(status=200, data={'count': self.city_news.view_count})
        return Response(status=400, data={'id error': self.city_news_id})
