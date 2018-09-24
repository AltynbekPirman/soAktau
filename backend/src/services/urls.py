from rest_framework.routers import SimpleRouter

from services.views import ServiceViewSet


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r'services', ServiceViewSet)
urlpatterns = router.urls
