
from itertools import product
from rest_framework.views import APIView

from .models import foodsale
from .serializers import foodsaleSerializer
from rest_framework.response import Response


class foodAPI(APIView):
    def get(self, request,pt=None, pk=None, format=None):
        id=pt
        if id is not None:
            stu = foodsale.objects.filter(Product=id).values()[:5]
            serializer = foodsaleSerializer(stu,many=True)
            return Response(serializer.data)

        stu = foodsale.objects.all()
        serializer = foodsaleSerializer(stu, many=True)
        return Response(serializer.data)

# from rest_framework import filters
# from rest_framework import generics

# from .models import foodsale
# from .serializers import foodsaleSerializer

# class foodAPIView(generics.ListCreateAPIView):
#     search_fields = ['Product']
#     filter_backends = (filters.SearchFilter,)
#     queryset = foodsale.objects.all()
#     serializer_class = foodsaleSerializer