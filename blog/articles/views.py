from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from rest_framework import viewsets
from .serializers import *

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request):
        permission_classes = (IsAuthenticated,)
        return viewsets.ModelViewSet.create(self, request)

    def update(self, request, pk=None):
        permission_classes = (IsAuthenticated,)
        return viewsets.ModelViewSet.update(self, request, pk)

    def partial_update(self, request, pk=None):
        permission_classes = (IsAuthenticated,)
        return viewsets.ModelViewSet.partial_update(self, request, pk)

    def destroy(self, request, pk=None):
        permission_classes = (IsAuthenticated,)
        return viewsets.ModelViewSet.destroy(self, request, pk)