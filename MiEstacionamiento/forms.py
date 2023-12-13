from django import forms
from django.contrib.auth.forms import AuthenticationForm


class RegistroForm(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=150)
    last_name = forms.CharField(label="Apellido", max_length=150)
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    email = forms.EmailField(label="Correo electrónico")


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class TarjetaForm(forms.ModelForm):
    num_tarjeta = forms.CharField(label="Número de tarjeta", max_length=16)
    fecha_venc = forms.DateField(label="Fecha de vencimiento")
    cvv = forms.CharField(label="CVV", max_length=3)
    widgets = {"fecha_venc": forms.DateInput(attrs={"type": "month"})}
