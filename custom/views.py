from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Custom
from .serializers import CustomSerializers
from django.core import serializers



@api_view(['GET'])
def update_custom(request):
    isError = False

    if request.method == "GET":
        queryset = Custom.objects.raw('SELECT Plantation_plantation.id, Plantation_plantation.code_accession, '
                                      'Plantation_plantation.nombre_plante, COALESCE(SUM('
                                      'Recolte_recolte.nombre_fruit_recolter),0) AS fruits_recolter, COALESCE(SUM('
                                      'Graine_graine.nombre_graine_extraite),0) as graine_recolter, '
                                      'Plantation_plantation.graine_objectif FROM Plantation_plantation LEFT '
                                      'JOIN Plante_plante ON Plantation_plantation.code_lot_plante = '
                                      'Plante_plante.code_lot_plante_id LEFT JOIN Recolte_recolte ON '
                                      'Plante_plante.code_plante = Recolte_recolte.code_plante_id LEFT JOIN '
                                      'Graine_graine ON Recolte_recolte.code_recolte = Graine_graine.code_recolte_id '
                                      'GROUP BY Plantation_plantation.code_accession;')

        serializer = CustomSerializers(queryset, many=True)
        data = serializer.data
        for datum in data:
            serializer = CustomSerializers(data=datum)
            if serializer.is_valid():
                instance, created = serializer.get_or_create()
            else:
                base = Custom.objects.get(code_accession=datum['code_accession'])
                serializer = CustomSerializers(base, data=datum)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                    isError = True
        if isError:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Success", status=status.HTTP_200_OK)

        return JsonResponse(data, safe=False)


