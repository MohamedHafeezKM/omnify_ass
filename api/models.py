from ast import mod
from pyexpat import model
from django.db import models

# Create your models here.

class Class(models.Model):
  name=models.TextField()
  date_time=models.DateTimeField()
  instructor=models.TextField()
  available_slots=models.PositiveIntegerField(default=10)
  def __str__(self):
    return f'{self.name}-{self.date_time}'


class BookingList(models.Model):
  class_id=models.ForeignKey(Class,on_delete=models.CASCADE)
  client_name=models.TextField()
  client_email=models.EmailField()
