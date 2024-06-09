from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth.models import User
# from booking_app.models import User
from booking_app.models import HotelOwner
from booking_app.models import Hobby
from .paginations import FiveResultsSetPagination

# from .serializers import UserSerializer
from .serializers import UserModelSerializer
from .serializers import HotelOwnerSerializer
# from .serializers import HobbySerializer
from .serializers import HobbyModelSerializer


class SomeDataViewClass(APIView):
    def get(self, request, format=None):
        data = {"message": "Hello, world!"}
        return Response(data)

#
# class UserApiView(APIView):
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         user = UserSerializer(data=request.data)
#         if user.is_valid():
#             user.save()
#             return Response(user.data, status=status.HTTP_201_CREATED)
#         return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, format=None):
#         users = User.objects.get(pk=pk)
#         serializer = UserSerializer(users, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         user = User.objects.get(pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class UserListApiView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]  # SessionAuthentication, BasicAuthentication # TokenAuthentication
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['username', 'first_name', 'is_superuser', 'is_staff']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    ordering_fields = ['username', 'first_name', 'last_name']
    ordering = ['username']


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


# class HotelOwnerListApiView(generics.ListCreateAPIView):
#     queryset = HotelOwner.objects.all()
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['first_name', 'last_name', 'age', 'sex']
#     search_fields = ['first_name', 'last_name', 'age', 'sex']

class HotelOwnerApiView(APIView):
    queryset = HotelOwner.objects.all()

    def get(self, request, format=None):
        owners = HotelOwner.objects.all()
        serializer = HotelOwnerSerializer(owners, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        owner = HotelOwnerSerializer(data=request.data)
        if owner.is_valid():
            owner.save()
            return Response(owner.data, status=status.HTTP_201_CREATED)
        return Response(owner.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        owner = HotelOwner.objects.get(pk=pk)
        serializer = HotelOwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        owner = HotelOwner.objects.get(pk=pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class HobbyApiView(APIView):
#     def get(self, request, format=None):
#         hobbies = Hobby.objects.all()
#         serializer = HobbySerializer(hobbies, many=True)
#         return Response(serializer.data)


class HobbyListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Hobby.objects.all()
    serializer_class = HobbyModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'detail']
    search_fields = ['name', 'detail']
    ordering_fields = ['name']
    ordering = ['name']
    pagination_class = FiveResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class HobbyListApiView(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Hobby.objects.all()
#     serializer_class = HobbyModelSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})


# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})

