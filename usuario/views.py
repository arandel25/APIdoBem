from usuario.models import UsuarioModel
from rest_framework.viewsets import ModelViewSet

from usuario.serializers import UsuarioSerializer

class UsuarioView(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = UsuarioModel.objects.all()
    http_method_names = ["GET", "PATCH", "POST"]