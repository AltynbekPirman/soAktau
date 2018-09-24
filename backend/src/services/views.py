from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as filters

from services.models import Service
from services.serializers import ServiceSerializer, ServiceDetailSerializer


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
        queryset = Service.objects.all()
        service = get_object_or_404(queryset, pk=pk)
        serializer = ServiceDetailSerializer(service)
        return Response(serializer.data)

