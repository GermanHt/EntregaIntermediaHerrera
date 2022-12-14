from django.db import models

class Cellphone (models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.description} - {self.price}"

class Computer (models.Model):
    brand = models.CharField(max_length=20)
    model =  models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.description} - {self.price}"

class Accessorie (models.Model):
    brand = models.CharField(max_length=20)
    model =  models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.description} - {self.price}"
