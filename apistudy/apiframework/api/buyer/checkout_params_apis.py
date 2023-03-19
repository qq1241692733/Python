

from api.baseapi import BaseBuyerApi

class SetAddressIdApi(BaseBuyerApi):

    def __init__(self,address_id):
        super().__init__()
        self.url = f'{self.host}/trade/checkout-params/address-id/{address_id}'
        self.method = 'post'

class SetPayTypeApi(BaseBuyerApi):
    def __init__(self,payment_type='COD'):
        super().__init__()
        self.url = f'{self.host}/trade/checkout-params/payment-type'
        self.method = 'post'
        self.data = {
            'payment_type':payment_type
        }