from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import DestroyAPIView,CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class CreateUserview(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class DeleteApiView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'


class BasicView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self,request,*args, **kwargs):
        return Response(status=200)
    