from rest_framework import viewsets
from .models import ONG, Animal, ConsultaVeterinaria, Adotante
from .serializers import ONGSerializer, AnimalSerializer, ConsultaVeterinariaSerializer, AdotanteSerializer


class BaseViewSet(viewsets.ModelViewSet):
    """
    ViewSet customizada que sobrescreve o método de exclusão
    para usar o soft delete do modelo.
    """
    def perform_destroy(self, instance):
        #chama o método .delete() do nosso modelo
        instance.delete()


class ONGViewSet(BaseViewSet):
    # objects agora retorna só os ativos
    queryset = ONG.objects.all()
    serializer_class = ONGSerializer


class AnimalViewSet(BaseViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class ConsultaVeterinariaViewSet(BaseViewSet):
    queryset = ConsultaVeterinaria.objects.all()
    serializer_class = ConsultaVeterinariaSerializer
    
class AdotanteViewSet(BaseViewSet):
    queryset = Adotante.objects.all()
    serializer_class = AdotanteSerializer   