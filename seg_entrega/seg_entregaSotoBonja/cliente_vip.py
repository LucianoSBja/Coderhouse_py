from client import Client
import uuid

class ClientVIP(Client):
    def __init__(self, first_name, last_name, age:int, email, address, phone, discount_rate:float):
        super().__init__(first_name, last_name, age, email, address, phone)
        self.discount_rate = discount_rate
        self.referral_code = None
        self.referral_count = 0

    def get_discount_amount(self, total_price):
        return total_price * self.discount_rate

    def generate_referral_code(self):
        self.referral_code = uuid.uuid4().hex

    def add_referral(self):
        self.referral_count += 1

    def __str__(self):
        return f"\nCliente VIP:\n{super().__str__()}" \
               f"\nDescuento: {self.discount_rate}%" \
               f"\nCódigo de referencia: {self.referral_code}" \
               f"\nNúmero de referidos: {self.referral_count}"