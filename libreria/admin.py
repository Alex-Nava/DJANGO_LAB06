from django.contrib import admin
from .models import Libro, Usuario, Review

admin.register(Libro)
admin.register(Usuario)
admin.register(Review)