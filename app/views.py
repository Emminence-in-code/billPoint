from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def create_user_api_view(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    else:
        return Response({'error':'invalid data'},status=400)


class DeleteApiView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'


class BasicView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args, **kwargs):
        return Response(status=200)
    