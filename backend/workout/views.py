from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def getUser(request, pk):
    users = User.objects.get(id=pk)
    s = UserSerializer(users, many=False)
    return Response(s.data)

@api_view(['POST'])
def addUser(request):
    s = UserSerializer(data=request.data)
    if s.is_valid():
        s.save()
    return Response(s.data)