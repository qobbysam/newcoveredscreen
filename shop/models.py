from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def get_price(self, request):
        return self.price

    @property
    def code(self):
        return str(self.id)