from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from main.models import CompanyInfo, Address, ChatRoom, TaxiQuestion, TaxiInfo
from main.serializers import CompanyInfoSerializer, AddressSerializer, ChatSerializer, TaxiQuestionSerializer, \
    TaxiInfoSerializer


class CompanyInfoViewSet(GenericViewSet, ListModelMixin):
    queryset = CompanyInfo.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        news = CompanyInfoSerializer(queryset, many=True)
        kaz = [d['kaz'] for d in news.data]
        rus = [d['rus'] for d in news.data]
        return Response({'kaz': kaz, 'rus': rus})


class AddressViewSet(GenericViewSet, ListModelMixin):
    queryset = Address.objects.all()

    def list(self, requset, *args, **kwargs):
        queryset = self.get_queryset()
        news = AddressSerializer(queryset, many=True, )
        kaz = [d['kaz'] for d in news.data]
        rus = [d['rus'] for d in news.data]
        return Response({'kaz': kaz, 'rus': rus})


class ChatViewSet(GenericViewSet, ListModelMixin):
    queryset = ChatRoom.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        news = ChatSerializer(queryset, many=True, context={'request': request})
        kaz = [d['kaz'] for d in news.data]
        rus = [d['rus'] for d in news.data]
        return Response({'kaz': kaz, 'rus': rus})


class TaxiViewSet(GenericViewSet, ListModelMixin):
    queryset = TaxiInfo.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        news = TaxiInfoSerializer(queryset, many=True, context={'request': request})
        kaz = [d['kaz'] for d in news.data]
        rus = [d['rus'] for d in news.data]
        return Response({'kaz': kaz, 'rus': rus})


class TaxiQuestionViewSet(GenericViewSet, ListModelMixin, ):
    queryset = TaxiQuestion.objects.all()
    serializer_class = TaxiQuestionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        services = TaxiQuestionSerializer(queryset, many=True)
        kaz = [d['kaz'] for d in services.data]
        rus = [d['rus'] for d in services.data]
        return Response({'kaz': kaz, 'rus': rus})

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        question = TaxiQuestionSerializer(question)
        return Response(question.data)
