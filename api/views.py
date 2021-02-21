from rest_framework import generics, viewsets, permissions
from monitoring.models import Link
from .serializers import LinkSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated

# this code was written by book

# class LinkListView(generics.ListAPIView):
#     queryset = Link.objects.all()
#     serializer_class = LinkSerializer
#     authentication_classes = (BaseAuthentication, )
#     permission_classes = (IsAuthenticated, )
#
#
# class LinkDetailView(generics.RetrieveAPIView):
#     queryset = Link.objects.all()
#     serializer_class = LinkSerializer
#     authentication_classes = (BaseAuthentication, )
#     permission_classes = (IsAuthenticated, )

# this one was written by drf tutorial

#
# class LinkViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows links to be viewed or edited.
#     """
#     queryset = Link.objects.all()
#     serializer_class = LinkSerializer
#     permission_classes = [permissions.IsAuthenticated]


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from monitoring.models import Link
from .serializers import *


class LinkView(APIView):
    def get(self, request):
        links = Link.objects.filter(account__user=request.user)
        serializer = LinkSerializer(links, many=True)
        return Response({'links': serializer.data})


class LinkCreate(APIView):
    def post(self, request):
        print(request.data)
        serializer = LinkNameSerializer(data=JSONParser().parse(request)) # request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
