from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import dateutil.parser

from .models import Plante
from .serializers import PlanteSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_plantations(request):
    if request.method == "GET":
        queryset = Plante.objects.all()
        serializer = PlanteSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def plantation_add(request):
    global instance
    isError = False

    if request.method == 'POST':
        data = request.data['data']
        # print(data)
        for datum in data:
            datum['modifier_le'] = dateutil.parser.parse(datum['modifier_le'])
            datum['modifier_le'] = datum['modifier_le'].replace(tzinfo=None)
            # print(datum['modifier_le'])
            serializer = PlanteSerializers(data=datum)
            if serializer.is_valid():
                instance, created = serializer.get_or_create()
            else:
                plantation = Plante.objects.get(code_plante=datum['code_plante'])
                # print(plantation.modifier_le)
                serializer = PlanteSerializers(plantation, data=datum)
                if serializer.is_valid():
                    theDate = datum['modifier_le']
                    if plantation.modifier_le < theDate:
                        serializer.save()
                    # else:
                    #     print(plantation.modifier_le, " est plus récent que ", theDate)
                else:
                    print(serializer.errors)
                    isError = True
        if isError:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Success", status=status.HTTP_200_OK)
