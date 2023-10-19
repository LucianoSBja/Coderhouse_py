class Client:
    def __init__(self, first_name, last_name, age:int, email, address, phone ) :
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.address = address
        self.phone = phone
        self.shopping_cart = []

    def add_product_to_cart(self, product):
         self.shopping_cart.append(product)

    def make_purchase(self):
         total = sum(product.price for product in self.shopping_cart)
         print(f"Cliente {self.first_name} ha realizado una compra por un total de ${total}.")
         self.shopping_cart = []

    def __str__(self):
         return f"\nCliente: {self.first_name}\nEmail: {self.email}\nDirección: {self.address}\nTeléfono: {self.phone}"
    

