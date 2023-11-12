from django.urls import path
from .views import crear_producto,lista_productos,detalle_producto, crear_categoria

urlpatterns = [
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('crear_categoria/', crear_categoria, name='crear_categoria'),
    path('crear_producto/', crear_producto, name='crear_producto'),   
]