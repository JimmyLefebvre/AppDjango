from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Base
from .serializers import BaseSerializers

@api_view(['GET'])
def get_base(request):
    if request.method == "GET":
        queryset = Base.objects.all()
        serializer = BaseSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
