from django import forms
from .models import Insumo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from .validators import OnlyLetters


class CustomUserCreationForm(UserCreationForm):
    nombre = forms.CharField(required=True,min_length=3,max_length=80, validators=[OnlyLetters()])
    apellidos = forms.CharField(required=True,min_length=3,max_length=80, validators=[OnlyLetters()])
    email = forms.EmailField(required=True,label="Dirección de correo electrónico")
    def clean_email(self):
        email = self.cleaned_data["email"]
        existe = User.objects.filter(email__iexact=email).exists()

        if existe:
           raise ValidationError("Este correo ya se encuentra registrado")

    class Meta:
        model = User
        fields = ["nombre","apellidos","email","username","password1","password2"]
    pass

class InsumoForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Insumo
        fields = '__all__'
        labels = {
            'descripcion' : 'Descripción'
        }