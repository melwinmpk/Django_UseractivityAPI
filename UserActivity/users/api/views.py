from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from users.models import Userdata, ActivityPeriod
from .serializers import UserSerializer, UsrActivitySerializer
import json


class UserListSerializerAPIView(mixins.CreateModelMixin,
                            generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        request = self.request
        qs = Userdata.objects.filter(
            user=self.request.id)
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, format=None):
        qs = Userdata.objects.all()
        serializer_class = UserSerializer(qs, many=True)
        return Response(serializer_class.data)  
                            

class UserSerializerAPIView(mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_object(self, *args, **kwargs):  # slug method for handeling the
        kwargs = self.kwargs
        kw_id = self.request.data.get('id')
        qs = Userdata.objects.get(id=kw_id)
        return qs

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 

    def patch(self, request, *args, **kwargs):    
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class UsrActivityListSerializerAPIView(mixins.CreateModelMixin,
                                   generics.ListAPIView):
    serializer_class = UsrActivitySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(userid=Userdata.objects.get(
            id=self.request.data.get("userid")))

    def get(self, request, format=None):
        userid = request.data.get("userid", None)
        qs = ActivityPeriod.objects.filter(
            userid=userid)
        serializer_class = UsrActivitySerializer(qs, many=True)
        return Response(serializer_class.data)


class UsrActivitySerializerAPIView(mixins.DestroyModelMixin,
                                   mixins.UpdateModelMixin,
                                   generics.RetrieveAPIView):
    serializer_class = UsrActivitySerializer
    lookup_field = 'id'

    def get_object(self, *args, **kwargs):  # slug method for handeling the
        kwargs = self.kwargs
        kw_id = self.request.data.get('id')
        qs = ActivityPeriod.objects.get(id=kw_id)
        return qs

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


class UserAPIView(APIView):
    pass
