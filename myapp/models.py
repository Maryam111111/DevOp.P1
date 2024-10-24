from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_available = models.IntegerField()
    car_id = models.IntegerField(unique=True)

    def __str__(self):
        return (f'Car ID:{self.car_id} name: {self.name} '
                f'price: {self.price} number_available: {self.number_available}')