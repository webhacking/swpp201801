from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from promises.models import Promise
from promises.serializers import PromiseSerializer, PromiseSerializerUpdate
from rest_framework.response import Response
from django.contrib.auth.models import User
from promises.serializers import UserSerializer, UserAllSerializer
from datetime import datetime
from rest_framework import permissions
from promises.permissions import IsUserOrReadOnly

class PromiseList(generics.ListCreateAPIView):
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, format=None):
        serializer = PromiseSerializer(data=request.data)

        if serializer.is_valid():
            if (request.data['sinceWhen'] < request.data['tilWhen']) and (int(self.request.user.id) != int(request.data['user2'])):
                serializer.save(user1=self.request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                pass
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PromiseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializerUpdate
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly,)

    def put(self, request, pk, format=None):

        promise = self.get_object()
        serializer = PromiseSerializerUpdate(promise, data=request.data)
        if serializer.is_valid():
            print(request.data)
            if request.data['sinceWhen'] < request.data['tilWhen']:
                serializer.save()
                return Response(serializer.data)
            else:
                pass
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAllList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserAllSerializer

class UserAllDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAllSerializer
