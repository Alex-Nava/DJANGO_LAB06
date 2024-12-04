from django import forms
from .models import Libro, Usuario, Review

# Formulario para el modelo Libro
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre', 'autor', 'publicacion']


# Formulario para el modelo Usuario
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'contraseña']


# Formulario para el modelo Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['libro', 'usuario','contenido']