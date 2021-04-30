from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from datetime import  datetime
import dateutil.parser
from dateutil.tz import UTC

from .models import Plantation
from .serializers import PlantationSerializers

@api_view(['GET'])
def get_plantations(request):
    if request.method == "GET":
        queryset = Plantation.objects.all()
        serializer = PlantationSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'POST'])
def plantation_add(request):
    global instance
    isError = False

    if request.method == 'POST':
        data = request.data['data']
        print(data)
        for datum in data:
            datum['modifier_le'] = dateutil.parser.parse(datum['modifier_le'])
            datum['modifier_le'] = datum['modifier_le'].replace(tzinfo=None)
            print(datum['modifier_le'])
            serializer = PlantationSerializers(data=datum)
            if serializer.is_valid():
                instance, created = serializer.get_or_create()
            else:
                plantation = Plantation.objects.get(code_plante=datum['code_plante'])
                print(plantation.modifier_le)
                serializer = PlantationSerializers(plantation, data=datum)
                if serializer.is_valid():
                    theDate = datum['modifier_le']
                    if plantation.modifier_le < theDate:
                        serializer.save()
                    else:
                        print(plantation.modifier_le, " est plus récent que ", theDate)
                else:
                    print(serializer.errors)
                    isError = True
        if isError:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Success", status=status.HTTP_200_OK)
