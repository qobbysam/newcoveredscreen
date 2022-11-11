# from locale import currency
# from time import timezone
# from django.db import models

# # Create your models here.
# class SquarePaymentTransaction(models.Model):
#     order_number = models.CharField(max_length=255)

#     reference = models.CharField(max_length=255)
#     status = models.CharField(max_length=255, blank=True)

#     amount = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
#     currency = models.CharField(max_length=3)
#     date_created = models.DateField(default=timezone.now)

#     class Meta:
#         ordering = ('-date_created',)

#     def __str__(self):

#         return u' Order %s - ref: %s, status: %s' % (self.order_number, self.reference, self.status)

    
#     def __unicode__(self):
#         return str(self)


