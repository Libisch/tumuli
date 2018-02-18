from biography.models import Memoir
from biography.serializers import MemoirSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view


# Period, Biography, ContentAtom

# PeriodSerializer, BiographySerializer, ContentAtomSerializer

class MemoirList(APIView):
    """
    List all code memoirs, or create a new memoir.
    """
    def get(self, request, format=None):
        memoirs = Memoir.objects.all()
        serializer = MemoirSerializer(memoirs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MemoirSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemoirDetails(APIView):
    """
    Retrieve, update or delete a memoir.
    """
    def get_object(self, pk):
        try:
            memoir = Memoir.objects.get(pk=pk)
        except Memoir.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        memoir = self.get_object(pk)
        serializer = MemoirSerializer(memoir)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        memoir = self.get_object(pk)
        serializer = MemoirSerializer(memoir, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        memoir = self.get_object(pk)
        memoir.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
 


#  def memoir_details(request, pk, format=None):
    # """
    # Retrieve, update or delete a memoir.
    # """
#     try:
#         memoir = Memoir.objects.get(pk=pk)
#     except Memoir.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MemoirSerializer(memoir)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = MemoirSerializer(memoir, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         memoir.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)