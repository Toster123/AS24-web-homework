from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', ArticleViewSet.as_view({'get': 'list'})),
    path('', ArticleViewSet.as_view({'post': 'create'})),
    path('<int:pk>', ArticleViewSet.as_view({'get': 'retrieve'})),
    path('<int:pk>', ArticleViewSet.as_view({'put': 'update'})),
    path('<int:pk>', ArticleViewSet.as_view({'put': 'partial_update'})),
    path('<int:pk>', ArticleViewSet.as_view({'put': 'destroy'})),
]