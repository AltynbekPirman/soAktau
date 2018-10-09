from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as filters

from services.models import Service, SubService, Title, Post, CalcParameter, CalcQuestion
from services.serializers import ServiceSerializer, SubServiceSerializer, TitleSerializer, \
    PostTextSerializer, TitleDetailSerializer, CalcParameterSerializer, CalcQuestionSerializer


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
        sub_services = SubServiceSerializer(queryset, many=True, context={'service_id': pk})
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
        titles = TitleSerializer(queryset, many=True,
                                 context={'service_id': self.service, 'sub_service_id': self.sub_service})

        # if SubService.objects.get(id=self.sub_service).code == 'calc':
        #     return Response({'calc': True, 'serviceId': self.service, 'subServiceId': self.sub_service})

        kaz = [d['kaz'] for d in titles.data]
        rus = [d['rus'] for d in titles.data]
        return Response({'kaz': kaz, 'rus': rus})

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Post.objects.filter(service_id=self.service, sub_service_id=self.sub_service, title_id=pk)
        serialized_title = PostTextSerializer(queryset, many=True)
        kaz = [d['kaz'] for d in serialized_title.data]
        rus = [d['rus'] for d in serialized_title.data]
        return Response({'kaz': kaz, 'rus': rus})


class CalcParameterViewSet(GenericViewSet, ListModelMixin):
    queryset = CalcParameter.objects.all()
    serializer_class = CalcParameterSerializer


class CalcQuestionViewSet(GenericViewSet, ListModelMixin, ):
    queryset = CalcQuestion.objects.all()
    serializer_class = CalcQuestionSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ServiceFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        services = CalcQuestionSerializer(queryset, many=True)
        kaz = [d['kaz'] for d in services.data]
        rus = [d['rus'] for d in services.data]
        return Response({'kaz': kaz, 'rus': rus})

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        question = CalcQuestionSerializer(question)
        return Response(question.data)
