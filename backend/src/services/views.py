from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as filters

from services.models import Service, SubService, Title, Post
from services.serializers import ServiceSerializer, SubServiceSerializer, TitleSerializer, \
    PostTextSerializer, TitleDetailSerializer


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
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ServiceFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('order_in_list', '-created_date'))
        services = ServiceSerializer(queryset, many=True, context={'request': request})
        kaz = [d['kaz'] for d in services.data]
        rus = [d['rus'] for d in services.data]
        return Response({'kaz': kaz, 'rus': rus})

    def retrieve(self, request, pk=None):
        queryset = SubService.objects.filter(posts__service=pk).order_by('order_in_list', '-created_date').distinct()
        sub_services = SubServiceSerializer(queryset, many=True)
        kaz = [d['kaz'] for d in sub_services.data]
        rus = [d['rus'] for d in sub_services.data]
        return Response({'kaz': kaz, 'rus': rus})


class TitleViewSet(GenericViewSet, ListModelMixin):

    serializer_class = TitleSerializer

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.service = self.kwargs.get('service')
        self.sub_service = self.kwargs.get('sub_service')

    def get_queryset(self, *args):
        return Title.objects.filter(posts__service=self.service, posts__sub_service=self.sub_service).distinct()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('order_in_list', '-created_date'))
        titles = TitleSerializer(queryset, many=True)
        kaz = []; rus = []
        for d in titles.data:
            d['kaz']['service_id'] = self.service
            d['kaz']['sub_service_id'] = self.sub_service
            d['rus']['service_id'] = self.service
            d['rus']['sub_service_id'] = self.sub_service
            kaz.append(d['kaz'])
            rus.append(d['rus'])
        return Response({'kaz': kaz, 'rus': rus})

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        title = get_object_or_404(queryset, pk=pk)
        serialized_title = TitleDetailSerializer(title)
        kaz = [d['kaz'] for d in serialized_title.data['posts']]
        rus = [d['rus'] for d in serialized_title.data['posts']]
        return Response({'kaz': kaz, 'rus': rus})
