from re import I
from django.urls import include
from django.urls.conf import path
from rest_framework import routers
from .views import TodosViewsets

router=routers.DefaultRouter()
router.register(r'todos', TodosViewsets)