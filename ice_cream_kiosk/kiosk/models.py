from django.db import models

# Create your models here.

class Kiosk(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IceCream(models.Model):
    FLAVOR_CHOICES = [
        ('banana', 'Banana'),
        ('salt caramel', 'Salt Caramel'),
        ('popcorn', 'Popcorn'),
    ]

    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    kiosk = models.ForeignKey(Kiosk, on_delete=models.CASCADE, related_name='ice_creams')

    def __str__(self):
        return f"{self.name} ({self.flavor})"


class Parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return f"{self.name}, {self.age}"
