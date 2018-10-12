from my_city.views import CityNewsViewSet
from rest_framework.routers import SimpleRouter


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r'my_city', CityNewsViewSet)
urlpatterns = router.urls
