from seg_entregaSotoBonja.client import Client
from seg_entregaSotoBonja.cliente_vip import ClientVip



cliente_regular = Client("Juan", "Pérez", 23, "juan.perez@example.com", "Calle 123, Ciudad de México", "555-555-5555")


cliente_vip = ClientVip("María", "García", 18, "maria.garcia@example.com", "Avenida 456, Guadalajara", "333-333-3333")

print(cliente_regular)
print(cliente_vip)