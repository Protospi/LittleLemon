from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    inventory = models.IntegerField()
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu items'