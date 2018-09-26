from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as filters

from services.models import Service, SubService, Title, Post
from services.serializers import ServiceSerializer, ServiceDetailSerializer, SubServiceSerializer, TitleSerializer, \
    PostTextSerializer


def get_language_filter(_model_):

    class IntermediateLanguageFilter(filters.FilterSet):
        lang = filters.CharFilter(field_name="language__code")

        class Meta:
            model = _model_
            fields = ('lang',)

    return IntermediateLanguageFilter


ServiceFilter = get_language_filter(Service)


class ServiceViewSet(GenericViewSet, ListModelMixin, ):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    ordering = ('-created_date', )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ServiceFilter

    def retrieve(self, request, pk=None):
        queryset = SubService.objects.filter(posts__service=pk).distinct()
        sub_services = SubServiceSerializer(queryset, many=True)
        return Response(sub_services.data)


class TitleViewSet(GenericViewSet, ListModelMixin):

    serializer_class = TitleSerializer

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.service = self.kwargs.get('service')
        self.sub_service = self.kwargs.get('sub_service')

    def get_queryset(self, *args):
        return Title.objects.filter(posts__service=self.service, posts__sub_service=self.sub_service).distinct()

    # def retrieve(self, request, pk=None, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     title = get_object_or_404(queryset, pk=pk)
    #     serializer = TitleDetailSerializer(title)
    #     return Response(serializer.data)


class PostViewSet(GenericViewSet, ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostTextSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        title = get_object_or_404(queryset, pk=pk)
        serializer = PostTextSerializer(title)
        return Response(serializer.data)
