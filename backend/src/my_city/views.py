from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from my_city.models import CityNews
from my_city.serializers import CityNewsSerializer


class CityNewsViewSet(GenericViewSet, ListModelMixin, ):
    queryset = CityNews.objects.all()
    serializer_class = CityNewsSerializer
    ordering = ('-created_date', )

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
