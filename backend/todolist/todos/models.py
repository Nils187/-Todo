from django.db import models

# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    users = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    importance = models.SmallIntegerField(null=True, blank=True)
    
    