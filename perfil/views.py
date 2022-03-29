from rest_framework.viewsets import ModelViewSet
from perfil.models import PerfilModel
from perfil.serializers import PerfilCreateSerializer, PerfilSerializer
from rest_framework import status
from rest_framework.response import Response

from perfil.service import PerfilService

class PerfilView(ModelViewSet):
    service_class = PerfilService
    serializer_class = PerfilSerializer
    queryset = PerfilModel.objects.all()
    http_method_names = ["GET", "PATCH", "POST"]

    def create(self, request, *args, **kwargs):
            serializer = PerfilCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = self.service_class.buscar_cep(request.data.get('cep'))
            if data is None:
                return Response({"message":"Erro para buscar o cep"}, status=status.HTTP_400_BAD_REQUEST)
            
            data = self.service_class.create_to_save(data, request.data)
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
