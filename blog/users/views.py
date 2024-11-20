from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import *
from django.contrib.auth.models import User

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer