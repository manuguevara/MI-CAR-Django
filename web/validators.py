from django.forms import ValidationError

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
