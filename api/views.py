from django.shortcuts import render
from rest_framework.views import APIView
from .models import Patient
from .serializers import PatientSerializer,UserSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,CreateAPIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



# Create your views here.
# class PatientList(APIView):
#     serializer_class=PatientSerializer
#     authentication_classes=[SessionAuthentication]
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     throttle_classes=[AnonRateThrottle,UserRateThrottle]
#     filter_backends=[DjangoFilterBackend]
#     filterset_fields = ['name', 'contact']
#     def get(self,request,formate=None):
#         patients=Patient.objects.all()
#         serializer=PatientSerializer(patients,many=True)
#         return Response(serializer.data)

    
#     def post(self,request,format=None):
#         serializer=PatientSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# class UserCreate(CreateAPIView,ListAPIView):
#     queryset=User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = ()
#     permission_classes = ()

class PatientList(ListAPIView):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['name', 'contact']
class UserCreate(CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]

class LoginView(APIView):
    serializer_class =UserSerializer
    permission_classes = [IsAuthenticated]
    def post(self,request,):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        if user:
            return Response({'token':user.auth_token.key,'User':user.username})
        else:
            return Response({'error':'Wrong credentials'},status=status.HTTP_400_BAD_REQUEST)