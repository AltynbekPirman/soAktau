from django.shortcuts import render
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from main.models import CompanyInfo, Address, ChatRoom
from main.serializers import CompanyInfoSerializer, AddressSerializer, ChatSerializer


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
