from rest_framework.routers import SimpleRouter

from services.views import ServiceViewSet, TitleViewSet


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r'services', ServiceViewSet)
router.register(r'services/(?P<service>\w+)/(?P<sub_service>\w+)', TitleViewSet, 'posts')
# router.register(r'posts', PostViewSet)
# router.register(r'services/(?P<service>\w+)/(?P<sub_service>\w+)/(?P<title>\w+)', PostListViewSet, 'posts')

urlpatterns = router.urls
