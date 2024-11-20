from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        permission_classes = []

        if self.action not in ('list', 'retrieve'):
            permission_classes.append(IsAuthenticated)

        return (permission() for permission in permission_classes)

    def get_queryset(self):
        if self.action in ('retrieve',):
            return Article.objects.all()
        elif self.action in ('list',):
            if self.request.query_params.get('author') is not None:
                return Article.objects.filter(author=self.request.query_params.get('author'))
            else:
                return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request):
        return viewsets.ModelViewSet.create(self, request)

    def update(self, request, *args, **kwargs):
        return viewsets.ModelViewSet.update(self, request, *args, **kwargs)

    def partial_update(self, request, pk=None):
        return viewsets.ModelViewSet.partial_update(self, request, pk)

    def destroy(self, request, pk=None):
        return viewsets.ModelViewSet.destroy(self, request, pk)