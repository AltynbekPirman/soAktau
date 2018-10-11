from rest_framework.routers import SimpleRouter

from main.views import CompanyInfoViewSet, AddressViewSet, ChatViewSet


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r'about', CompanyInfoViewSet)
router.register(r'address', AddressViewSet)
router.register(r'chats', ChatViewSet)
urlpatterns = router.urls
