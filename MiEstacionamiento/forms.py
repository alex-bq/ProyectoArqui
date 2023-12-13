from django import forms
from django.contrib.auth.forms import AuthenticationForm


class RegistroForm(forms.Form):
    ROLE = [
        ("cliente", "Cliente"),
        ("dueno", "Dueño"),
    ]
    rol = forms.ChoiceField(label="Rol", choices=ROLE)
    first_name = forms.CharField(label="Nombre", max_length=150)
    last_name = forms.CharField(label="Apellido", max_length=150)
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    email = forms.EmailField(label="Correo electrónico")


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
