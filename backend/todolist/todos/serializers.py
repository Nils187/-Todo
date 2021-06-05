from django.db.models import fields
from .models import Todos
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = "__all__"
