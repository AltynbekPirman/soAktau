from rest_framework import routers

from news.views import NewsViewSet, AnnouncementViewSet, QuestionViewSet
from rest_framework.routers import SimpleRouter


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r'news', NewsViewSet)
router.register(r'questions/(?P<lang_code>\w+)', QuestionViewSet)
router.register(r'announcements', AnnouncementViewSet)
urlpatterns = router.urls
