from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):

    username = forms.CharField(
        label="Nombre de usuario",
        error_messages={
        'required': 'Este campo es obligatorio.',
        'unique': 'Este nombre de usuario ya está en uso.'
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Tu nombre de usuario',
            'class': 'registro_form-text'
        })
    )
    
    email = forms.EmailField(
        required=True,
        label="Correo electrónico",
        error_messages={
        'required': 'Este campo es obligatorio.',
        'unique': 'Este email ya está en uso.'
        },
        widget=forms.EmailInput(attrs={
            'placeholder': 'ejemplo@correo.com',
            'class': 'registro_form-text'
        })
    )

    password1 = forms.CharField(
        label="Contraseña",
        error_messages={
        'required': 'Este campo es obligatorio.'
        },
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Ingresá tu contraseña',
            'class': 'registro_form-text'
        })
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        error_messages={
        'required': 'Este campo es obligatorio.'
        },
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repetí la contraseña',
            'class': 'registro_form-text'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PerfilUsuarioForm(forms.ModelForm):
    first_name = forms.CharField(
        required=False,
        label="Nombre",
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre(s)',
            'class': 'registro_form-text'
        })
    )
    last_name = forms.CharField(
        required=False,
        label="Apellido",
        widget=forms.TextInput(attrs={
            'placeholder': 'Apellido(s)',
            'class': 'registro_form-text'
        })
    )

    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={
            'placeholder': 'Tu nombre de usuario',
            'class': 'registro_form-text'
        })
    )

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'ejemplo@correo.com',
            'class': 'registro_form-text'
        })
    )
    
    # Nuevos campos para cambio de contraseña
    password1 = forms.CharField(
        label="Nueva contraseña",
        required=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Ingresá una nueva contraseña',
            'class': 'registro_form-text'
        })
    )
    password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        required=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repetí la nueva contraseña',
            'class': 'registro_form-text'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 or p2:
            if p1 != p2:
                self.add_error('password2', "Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password1")

        if password:
            user.set_password(password)  # cambia la contraseña correctamente

        if commit:
            user.save()

        return user