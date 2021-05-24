from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework.response import Response
from django.db import connection

from .models import Plantation
from .serializers import PlantationSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_plantation(request):
    if request.method == "GET":
        queryset = Plantation.objects.all()
        serializer = PlantationSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_lot_graine_extraite(request, code_lot_plante):
    if request.method == "GET":
        sql = "SELECT sum(g.nombre_graine_extraite) as graines_total FROM Base_base b INNER JOIN " \
              "Plantation_plantation p ON b.code_lot_plante = p.code_lot_plante_id INNER JOIN Recolte_recolte r ON " \
              "p.code_plante = r.code_plante_id INNER JOIN Graine_graine g ON r.code_recolte = g.code_recolte_id " \
              "WHERE b.code_lot_plante = '" + code_lot_plante + "';"
        cursor = connection.cursor()
        cursor.execute(sql)
        max_value = cursor.fetchone()[0]
        return Response(max_value)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def plantation_add(request):
    global instance
    isError = False

    if request.method == 'POST':
        data = request.data['data']
        for datum in data:
            serializer = PlantationSerializers(data=datum)
            if serializer.is_valid():
                instance, created = serializer.get_or_create()
            else:
                base = Plantation.objects.get(code_lot_plante=datum['code_lot_plante'])
                serializer = PlantationSerializers(base, data=datum)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                    isError = True
        if isError:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Success", status=status.HTTP_200_OK)
