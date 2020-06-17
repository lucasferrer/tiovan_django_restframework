from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, \
    CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from tiovan_app.serializers import MotoristaSerializer, EnderecoSerializer,\
    UserSerializer, MotoristaDetailSerializer
from tiovan_app.models import Motorista, Endereco
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny # <-- Here
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    permission_classes_by_action = {'create': [AllowAny]}
    

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

class EnderecoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows endereços to be viewed or edited.
    """
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    permission_classes_by_action = {'create': [AllowAny]}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class MotoristaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows endereços to be viewed or edited.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Motorista.objects.select_related('endereco').select_related('user').all()
    serializer_class = MotoristaSerializer


    permission_classes_by_action = {'create': [AllowAny]}


    def list(self, request):
        # authentication_classes = [TokenAuthentication, BasicAuthentication]
        serializer_context = {
            'request': request,
        }
        queryset = Motorista.objects.select_related('endereco').select_related('user').all()
        serializer = MotoristaDetailSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        # authentication_classes = [TokenAuthentication, BasicAuthentication]
        # permission_classes = [IsAuthenticated]
        serializer_context = {
            'request': request,
        }
        queryset = Motorista.objects.select_related('endereco').select_related('user').all()
        motorista = get_object_or_404(queryset, pk=pk)
        serializer = MotoristaDetailSerializer(motorista, context=serializer_context)
        return Response(serializer.data)
    
    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]