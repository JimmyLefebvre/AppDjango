from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
import dateutil.parser

from .models import Graine
from .serializers import GraineSerializers


@api_view(['GET'])
def get_graines(request):
    if request.method == "GET":
        queryset = Graine.objects.all()
        serializer = GraineSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def recolte_add(request):
    global instance
    isError = False

    if request.method == 'POST':
        data = request.data['data']
        print(data)
        for datum in data:
            datum['modifier_le'] = dateutil.parser.parse(datum['modifier_le'])
            datum['modifier_le'] = datum['modifier_le'].replace(tzinfo=None)
            # print(datum['modifier_le'])
            serializer = GraineSerializers(data=datum)
            if serializer.is_valid():
                instance, created = serializer.get_or_create()
            else:
                graine = Graine.objects.get(code_recolte=datum['code_recolte'])
                # print(recolte.modifier_le)
                serializer = GraineSerializers(graine, data=datum)
                if serializer.is_valid():
                    theDate = datum['modifier_le']
                    if graine.modifier_le < theDate:
                        serializer.save()
                    # else:
                    #     print(recolte.modifier_le, " est plus récent que ", theDate)
                else:
                    print(serializer.errors)
                    isError = True
        if isError:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Success", status=status.HTTP_200_OK)
