from rest_framework.routers import SimpleRouter

from main.views import CompanyInfoViewSet, AddressViewSet, ChatViewSet, TaxiQuestionViewSet, TaxiViewSet


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r'about', CompanyInfoViewSet)
router.register(r'address', AddressViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'taxi/questions', TaxiQuestionViewSet)
router.register(r'taxi/data', TaxiViewSet)
urlpatterns = router.urls
