from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>/', UserRetrieveAPIView.as_view()),
]
