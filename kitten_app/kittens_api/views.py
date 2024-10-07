from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from .models import Breed, Kitten, Rating
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BreedSerializer, KittenSerializer, RatingSerializer
from django.utils.functional import SimpleLazyObject
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user
# Create your views here.

from rest_framework import generics



class BreedListView(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenListView(generics.ListAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer

    def get_queryset(self):
        breed_id = self.request.query_params.get('breed', None)
        if breed_id:
            return Kitten.objects.filter(breed__id=breed_id)
        return super().get_queryset()
    

class KittenDetailView(generics.RetrieveAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer


class KittenCreateView(generics.CreateAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        # Если пользователь ленивый объект, получаем реальный экземпляр
        if isinstance(user, SimpleLazyObject):
            user = user._wrapped if hasattr(user, '_wrapped') else user
        
        serializer.save(owner=user)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Доступ только владельцу котенка для изменения или удаления
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class KittenUpdateView(generics.UpdateAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class KittenDeleteView(generics.DestroyAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class KittenRatingView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    '''
    Здесь вщзникла трудность - не получается получить объект пользователя
    Точнее, получается, но не тот, который нужен
    Выпадает ошибка при попытке получить объект пользователя
    ValueError: Cannot assign "<User: root>": "Kitten.owner" must be a "User" instance.
    '''

    def post(self, request, pk):
        user = get_object_or_404(User, pk=request.user.id)
        print(f'Debug: user = {user}, user id = {user.id}, user type = {type(user)}')
        print(f'Debug: request data = {request.data}')
        
        kitten = get_object_or_404(Kitten, pk=pk)
        print(f'Debug: kitten = {kitten}, kitten id = {kitten.id}, kitten type = {type(kitten)}')
        rating, created = Rating.objects.get_or_create(user=request.user, kitten=kitten)
        print(f'Debug: user = {request.user}, user id = {request.user.id}, user type = {type(request.user)}')

        
        serializer = RatingSerializer(rating, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        else:
            print(f'Debug: serializer errors = {serializer.errors}')
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)