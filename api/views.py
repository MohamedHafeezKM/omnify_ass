
from urllib import request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.models import BookingList,Class
from api.serializers import ClassSerializers,BookingListSerializers
# Create your views here.


class ClassView(APIView):
  def get(self,request,*args,**kwargs):
    qs=Class.objects.all().order_by('-id')
    deserializer=ClassSerializers(qs,many=True)
    return Response(data=deserializer.data)
  

class BookView(APIView):
  def get(self,request,*args,**kwargs):
    class_id=request.data.get('class_id')
    clas=Class.objects.get(id=class_id)
    if clas.available_slots==0:
      return Response(data={'message':'This class has been filled'})
    seriailzer=BookingListSerializers(data=request.data)
    if seriailzer.is_valid():
      seriailzer.save()
      clas.available_slots-=1
      clas.save()
      return Response(data=seriailzer.data,status=status.HTTP_201_CREATED)
    
    else:
      return Response(data=seriailzer.errors,status=status.HTTP_204_NO_CONTENT)
    
class BookingListView(APIView):
  def get(self,request,*args,**kwargs):
    email=request.data.get('client_email')
    qs=BookingList.objects.filter(client_email=email)
    deserializer=BookingListSerializers(qs,many=True)
    return Response(data=deserializer.data)