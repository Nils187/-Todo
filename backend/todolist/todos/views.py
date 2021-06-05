from .models import Todos
from rest_framework import viewsets
from .serializers import TodoSerializer


class TodosViewsets(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
