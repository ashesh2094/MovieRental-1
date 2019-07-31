from django.db import models

import Movies


class Movies(models.Model):
    name = models.CharField(max_length=30)
    actor = models.CharField(max_length=30)
    year = models.IntegerField()
    genre = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rented = models.ForeignKey('Customer.Customer',on_delete=models.SET_NULL,null=True,blank=True)




    def __str__(self):
        return self.name