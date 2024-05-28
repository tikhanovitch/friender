from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from booking_app.models import HotelOwner
from booking_app.models import Hobby
from .serializers import UserSerializer
from .serializers import HotelOwnerSerializer
from .serializers import HobbySerializer


class SomeDataViewClass(APIView):
    def get(self, request, format=None):
        data = {"message": "Hello, world!"}
        return Response(data)


class UserApiView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        users = User.objects.get(pk=pk)
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HotelOwnerApiView(APIView):
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


class HobbyApiView(APIView):
    def get(self, request, format=None):
        hobbies = Hobby.objects.all()
        serializer = HobbySerializer(hobbies, many=True)
        return Response(serializer.data)



# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})


# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})


