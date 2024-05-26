
from rest_framework.views import APIView
from rest_framework.response import Response
from booking_app.models import User


class SomeDataViewClass(APIView):
    def get(self, request, format=None):
        data = {"message": "Hello, world!"}
        return Response(data)

# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})


# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})


