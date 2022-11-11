import logging


from square.client import Client

from django.conf import settings
from django.core import exceptions



class Gateway:

    def __init__(self ) -> None:
        # self.source_id = source_id
        # self.idempotency_key = idempotency_key
        # self.amount = amount
        # self.currency = currency
        self.squareclient = Client(access_token=settings.SQUARE_ACCESS_TOKEN, environment=settings.SQUARE_ENVIRONMENT)

    
    def generate_body(self, source_id, idempotency_key, amount, currency):
        body = {
            'source_id' : source_id,
            'idempotency_key': str(idempotency_key),
            'amount_money': {
                "amount": amount,
                "currency": currency

            } ,
            'autocomplete': True,
        }
        print(body)
        return  body

    def create_payment_attempt(self, body):

        # body = {
        #     'source_id' : self.source_id,
        #     'idempotency_key': self.idempotency_key,
        #     'amount_money': {
        #         "amount": self.amount,
        #         "currency": self.currency

        #     }
        # }

        # self.squareclient = Client(access_token=settings.SQUARE_ACCESS_TOKEN, environment=settings.SQUARE_ENVIRONMENT)

        result = self.squareclient.payments.create_payment(body)

        print(result)

        return result
        

    