from django.db import connection
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Piments, Aubergines
from .serializers import PimentsSerializers, AuberginesSerializers


@api_view(['GET'])
def update_piments(request):
    isError = False

    if request.method == "GET":
        queryset = Piments.objects.raw(
            "Select ROW_NUMBER() OVER ( ORDER BY Plante_plante.id) IDLot, Plantation_plantation.code_accession AS PM, Plantation_plantation.lot_origine AS Type_de_lot, lieu as RefLieu, parcelle as Parcelle, Plante_plante.num_plante as Num_plante, COALESCE(SUM(Graine_graine.nombre_graine_extraite), 0) as Quantite, Plantation_plantation.lot_origine AS Lot_parent, Plante_plante.type_fecondation AS Pollinisation, MIN(DATE(Recolte_recolte.modifier_le)) AS Date_premiere_recolte, COALESCE(SUM(Recolte_recolte.nombre_fruit_recolter), 0) AS Nombre_de_fruits_recoltes, strftime('%Y', MIN(DATE(Recolte_recolte.modifier_le))) AS Annee, Plante_plante.code_plante AS Code_barre_lot FROM Plantation_plantation INNER JOIN Plante_plante ON Plantation_plantation.code_lot_plante = Plante_plante.code_lot_plante_id INNER JOIN Recolte_recolte ON Plante_plante.code_plante = Recolte_recolte.code_plante_id INNER JOIN Graine_graine ON Recolte_recolte.code_recolte = Graine_graine.code_recolte_id WHERE Plantation_plantation.code_lot_plante LIKE '%PI%' GROUP BY Code_barre_lot;")

        serializer = PimentsSerializers(queryset, many=True)

        data = serializer.data

        sql = "UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Access_piments';"

        Piments.objects.all().delete()
        cursor = connection.cursor()
        cursor.execute(sql)

        for datum in data:
            # print(datum)
            serializer = PimentsSerializers(data=datum)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                isError = True
        if isError:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
        else:
            return redirect("aubergines/")


@api_view(['GET'])
def update_aubergines(request):
    isError = False

    if request.method == "GET":
        queryset = Aubergines.objects.raw("Select ROW_NUMBER() OVER ( ORDER BY Plante_plante.id) ID, Plantation_plantation.code_accession as CodeMM, 'FAUX' as Lot_absent_jete_fini, strftime('%Y', MIN(DATE(Recolte_recolte.modifier_le))) AS Annee, Plantation_plantation.lot_origine AS Type_de_lot, lieu as Lieu, Plante_plante.num_plante as Num_plante, Plante_plante.type_fecondation AS Pollinisation, COALESCE(SUM(Graine_graine.nombre_graine_extraite), 0) as Quantite, parcelle as Parcelle, Plantation_plantation.lot_origine AS Lot_parent, MIN(DATE(Recolte_recolte.modifier_le)) AS Date_premiere_recolte, COALESCE(SUM(Recolte_recolte.nombre_fruit_recolter), 0) AS Nombre_de_fruits_recoltes, Plante_plante.code_plante AS Code_barre_lot, 'FAUX' as Long_terme, 'FAUX' as Lot_congele FROM Plantation_plantation INNER JOIN Plante_plante ON Plantation_plantation.code_lot_plante = Plante_plante.code_lot_plante_id INNER JOIN Recolte_recolte ON Plante_plante.code_plante = Recolte_recolte.code_plante_id INNER JOIN Graine_graine ON Recolte_recolte.code_recolte = Graine_graine.code_recolte_id WHERE Plantation_plantation.code_lot_plante LIKE '%AU%' GROUP BY Code_barre_lot;")

        serializer = AuberginesSerializers(queryset, many=True)

        data = serializer.data

        sql = "UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Access_aubergines';"

        Aubergines.objects.all().delete()
        cursor = connection.cursor()
        cursor.execute(sql)

        for datum in data:
            # print(datum)
            serializer = AuberginesSerializers(data=datum)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                isError = True
        if isError:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Success", status=status.HTTP_200_OK)
