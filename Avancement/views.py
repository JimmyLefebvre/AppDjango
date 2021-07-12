from django.db import connection
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import EnCours, NonFait
from .serializers import EnCoursSerializers, NonFaitSerializers


@api_view(['GET'])
def update_en_cours(request):
    isError = False

    if request.method == "GET":
        queryset = EnCours.objects.raw(
            'SELECT ROW_NUMBER() OVER ( ORDER BY Plantation_plantation.id) id, Plantation_plantation.code_accession, COALESCE(Plante_plante.num_plante, 0) as numero_plante, Plantation_plantation.nombre_plante, COALESCE(Plante_plante.num_plante, 0) || "_" || Plantation_plantation.lieu || "_" || Plantation_plantation.parcelle as num_lieu_parcelle, COALESCE(SUM(Recolte_recolte.nombre_fruit_recolter), 0) as fruits_recoltes_plante, COALESCE(SUM(Graine_graine.nombre_graine_extraite), 0) as graines_recoltees_plante, Plantation_plantation.graine_objectif as graines_objectif_accession FROM Plantation_plantation INNER JOIN Plante_plante ON Plantation_plantation.code_lot_plante = Plante_plante.code_lot_plante_id LEFT JOIN Recolte_recolte on Plante_plante.code_plante = Recolte_recolte.code_plante_id LEFT JOIN Graine_graine ON Recolte_recolte.code_recolte = Graine_graine.code_recolte_id GROUP BY Plante_plante.id')

        serializer = EnCoursSerializers(queryset, many=True)

        data = serializer.data

        sql = "UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Avancement_encours';"

        EnCours.objects.all().delete()
        cursor = connection.cursor()
        cursor.execute(sql)

        for datum in data:
            serializer = EnCoursSerializers(data=datum)
            if serializer.is_valid():
                instance, created = serializer.get_or_create()
            else:
                base = EnCours.objects.get(code_accession=datum['code_accession'], numero_plante=datum['numero_plante'])
                serializer = EnCoursSerializers(base, data=datum)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                    isError = True
        if isError:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
        else:
            return redirect("non_fait/")


@api_view(['GET'])
def update_non_fait(request):
    isError = False

    if request.method == "GET":
        queryset = NonFait.objects.raw(
            'SELECT ROW_NUMBER() OVER ( ORDER BY Plantation_plantation.id) id, Plantation_plantation.code_accession, COALESCE(Plante_plante.num_plante, 0) as numero_plante, Plantation_plantation.nombre_plante, COALESCE(Plante_plante.num_plante, 0) || "_" || Plantation_plantation.lieu || "_" || Plantation_plantation.parcelle as num_lieu_parcelle, COALESCE(SUM(Recolte_recolte.nombre_fruit_recolter), 0) as fruits_recoltes_plante, COALESCE(SUM(Graine_graine.nombre_graine_extraite), 0) as graines_recoltees_plante, Plantation_plantation.graine_objectif as graines_objectif_accession FROM Plantation_plantation LEFT JOIN Plante_plante ON Plantation_plantation.code_lot_plante = Plante_plante.code_lot_plante_id LEFT JOIN Recolte_recolte on Plante_plante.code_plante = Recolte_recolte.code_plante_id LEFT JOIN Graine_graine ON Recolte_recolte.code_recolte = Graine_graine.code_recolte_id WHERE numero_plante = 0 GROUP BY num_lieu_parcelle')

        NonFait.objects.all().delete()

        sql = "UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Avancement_nonfait';"
        cursor = connection.cursor()
        cursor.execute(sql)

        serializer = NonFaitSerializers(queryset, many=True)
        data = serializer.data
        for datum in data:
            serializer = NonFaitSerializers(data=datum)
            if serializer.is_valid():
                instance, created = serializer.get_or_create()
            else:
                base = NonFait.objects.get(code_accession=datum['code_accession'], numero_plante=datum['numero_plante'])
                serializer = NonFaitSerializers(base, data=datum)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                    isError = True
        if isError:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
        else:
            return redirect("piments/")

