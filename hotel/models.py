from django.db import models
from django.utils import timezone
# Create your models here. 
class costomer(models.Model):
    name = models.CharField( max_length=100)
    Phone = models.CharField(max_length=20)
    IDproof = models.CharField( max_length=100)
    ID_num = models.CharField(max_length=50)
    Adults = models.IntegerField()
    children = models.IntegerField()
    RoomCategory = models.CharField( max_length=50, default='none')
    CheckIN = models.DateField( auto_now=False, auto_now_add=False, default=timezone.now())
    CheckOUT = models.DateField( auto_now=False, auto_now_add=False, default=timezone.now())

class Rooms(models.Model):
    room_type = models.CharField(max_length=60)
    room_rent = models.DecimalField(max_digits=6, decimal_places=2)
    capacity = models.CharField(max_length=70)
    status = models.CharField(max_length=20)



    

    