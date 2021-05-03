from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
import dateutil.parser

from .models import Recolte
from .serializers import RecolteSerializers


@api_view(['GET'])
def get_recoltes(request):
    if request.method == "GET":
        queryset = Recolte.objects.all()
        serializer = RecolteSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def recolte_add(request):
    global instance
    isError = False

    if request.method == 'POST':
        data = request.data['data']
        # print(data)
        for datum in data:
            print(datum)
            datum['modifier_le'] = dateutil.parser.parse(datum['modifier_le'])
            datum['modifier_le'] = datum['modifier_le'].replace(tzinfo=None)
            # print(datum['modifier_le'])
            serializer = RecolteSerializers(data=datum)
            if serializer.is_valid():
                instance, created = serializer.get_or_create()
            else:
                recolte = Recolte.objects.get(code_recolte=datum['code_recolte'])
                # print(recolte.modifier_le)
                serializer = RecolteSerializers(recolte, data=datum)
                if serializer.is_valid():
                    theDate = datum['modifier_le']
                    if recolte.modifier_le < theDate:
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
