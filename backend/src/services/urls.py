from rest_framework.routers import SimpleRouter

from services.views import ServiceViewSet, TitleViewSet, CalcParameterViewSet, CalcQuestionViewSet


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r'services', ServiceViewSet)
router.register(r'services/(?P<service>\w+)/(?P<sub_service>\w+)', TitleViewSet, 'posts')
router.register(r'calc/parameters', CalcParameterViewSet)
router.register(r'calc/questions', CalcQuestionViewSet)

urlpatterns = router.urls
