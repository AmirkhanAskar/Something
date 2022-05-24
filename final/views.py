from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics, status
from django.contrib.auth.models import User
from .models import Book, Journal
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import BookSerializer, JournalSerializer, UserSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view


class BookViewSet(viewsets.ViewSet):
    # permission_classes_by_action = {'create': [IsAdminUser],
    #                                 'list': [AllowAny],
    #                                 'retrieve': [AllowAny],
    #                                 'destroy': [IsAdminUser]}

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid_input'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        book.delete()
        return Response({'success': 'Deleted'}, status=status.HTTP_200_OK)


class JournalViewSet(viewsets.ViewSet):
    # permission_classes_by_action = {'create': [IsAdminUser],
    #                                 'list': [AllowAny],
    #                                 'retrieve': [AllowAny],
    #                                 'destroy': [IsAdminUser]}
    def list(self, request):
        queryset = Journal.objects.all()
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Journal.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = JournalSerializer(book)
        return Response(serializer.data)

    def create(self, request):
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid_input'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Journal.objects.all()
        journal = get_object_or_404(queryset, pk=pk)
        journal.delete()
        return Response({'success': 'Deleted'}, status=status.HTTP_200_OK)


class UserCreateList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super(UserCreateList, self).post(request, *args, **kwargs)


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    s = serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)