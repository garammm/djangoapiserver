from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def index(request):
    data = {"request":"success","data":[{"id":"itstudy", "name": "람"}]}
    return Response(data, status=status.HTTP_200_OK)