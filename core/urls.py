from rest_framework.routers import DefaultRouter
from .views import ONGViewSet, AnimalViewSet, ConsultaVeterinariaViewSet, AdotanteViewSet

router = DefaultRouter()
router.register(r'ongs', ONGViewSet)
router.register(r'animais', AnimalViewSet)
router.register(r'consultas', ConsultaVeterinariaViewSet)
router.register(r'adotantes', AdotanteViewSet)

urlpatterns = router.urls
