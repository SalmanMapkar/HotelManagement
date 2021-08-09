from django.db.models.query import QuerySet
from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.response import Response


from .serializers import AccountSerializer
from .models import AccountUser


class getAccountView(viewsets.ModelViewSet):
    queryset = AccountUser.objects.all()
    serializer_class = AccountSerializer

    
    def list(self, request, username = None, password = None):
        if (self.queryset.filter(UserName = username, PassWord = password).count()==1):
            return Response({
                "status": True,
                "data": self.queryset.filter(UserName = username, PassWord = password).values()
            })
        else:
            return Response({
                "status": False
            })