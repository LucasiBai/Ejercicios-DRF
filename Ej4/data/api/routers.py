from rest_framework.routers import DefaultRouter

from data.api.views.hero_viewsets import HeroViewSet

router = DefaultRouter()
router.register(r"heroes", HeroViewSet)

urlpatterns = router.urls
