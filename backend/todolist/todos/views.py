from rest_framework import viewsets
from .models import Todos
from .serializers import TodoSerializer

class TodosViewsets(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer 
# Create your views here.
    def get_queryset(self):
        print(self.queryset)
        return self.queryset