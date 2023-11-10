from django import forms
from .models import Categoria, Producto, Orden

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'descripcion', 'precio']

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['productos']

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100)