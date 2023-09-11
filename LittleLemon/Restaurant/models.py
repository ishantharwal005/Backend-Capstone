from django.db import models
from django.utils import timezone

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
    name = models.CharField(db_column="name", max_length=255)
    noOfGuests = models.IntegerField(db_column="noofguests", default=6)
    # bookingdate = models.CharField(db_column="bookingdate")
    # booking_date = models.DateField(default=timezone.now)
    booking_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}: {self.booking_date}'
    
    class Meta:
        managed = True
        db_table = 'booking'

class Menu(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
    title = models.CharField(db_column="title", max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(db_column="inventory", default=5)
    def __str__(self):
        return f'{self.title}: ${self.price:.2f}'
    
    class Meta:
        managed = True
        db_table = 'menu'