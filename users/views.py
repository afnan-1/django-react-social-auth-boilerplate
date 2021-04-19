from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from .models import CustomUser

class CustomUserCreate(APIView):

    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            user = CustomUser.objects.get(pk=request.user.id)
            print(user._meta.fields)
            serializer = CustomUserSerializer(user,many=False)
            return Response(serializer.data)
        else:
            return Response({'ok':"ok"})