from django.forms import ValidationError
from .models import Insumo

class OnlyLetters:
    def __call__(self, value):
        texto = value
        minCharMayus = 65
        maxCharMayus = 90
        minCharMinus = 97
        maxCharMinus = 122
        for c in range(len(texto)):
            ascii = ord(texto[c])
            if texto[c] != ' ' and (ascii<=minCharMayus or(ascii>maxCharMayus and ascii<minCharMinus)or ascii>maxCharMinus):
                raise ValidationError("Por favor ingrese solo letras.")
        return value
class UniqueUpperLower:
    def __call__(self, value):
        insumos = Insumo.objects.all()
        for n in insumos:
            if value.lower() == n.nombre.lower():
                raise ValidationError("El insumo ingresado ya existe, por favor revise e intente nuevamente.")
            else:
                return value
            