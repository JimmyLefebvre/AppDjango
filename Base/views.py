from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponseServerError
from rest_framework.response import Response

from .models import Base
from .serializers import BaseSerializers


@api_view(['GET'])
def get_base(request):
    if request.method == "GET":
        queryset = Base.objects.all()
        serializer = BaseSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def base_add(request):
    global instance
    isError = False

    if request.method == 'POST':
        data = request.data['data']
        for datum in data:
            serializer = BaseSerializers(data=datum)
            if serializer.is_valid():
                instance, created = serializer.get_or_create()
            else:
                base = Base.objects.get(code_lot_plante=datum['code_lot_plante'])
                serializer = BaseSerializers(base, data=datum)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                    isError = True
        if isError:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Success", status=status.HTTP_200_OK)
