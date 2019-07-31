from django.db import models
# from django.core.exceptions import ValidationError
# from django.core.validators import RegexValidator


class Customer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name

