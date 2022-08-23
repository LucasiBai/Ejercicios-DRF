from unicodedata import name
from rest_framework.routers import DefaultRouter
from .views.cart_viewsets import CartItemApi

router = DefaultRouter()
router.register(r"articulos", CartItemApi)

urlpatterns = router.urls
