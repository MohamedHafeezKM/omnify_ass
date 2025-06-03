
from rest_framework import serializers
from api.models import BookingList,Class
class ClassSerializers(serializers.ModelSerializer):
  class Meta:
    model=Class
    fields='__all__'

class BookingListSerializers(serializers.ModelSerializer):
  class Meta:
    model=BookingList
    fields='__all__'