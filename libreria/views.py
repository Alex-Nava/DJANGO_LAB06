from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Libro, Usuario, Review
from .forms import LibroForm, UsuarioForm, ReviewForm

# Vista para crear un nuevo libro
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')  # Redirige a la lista de libros
    else:
        form = LibroForm()

    return render(request, 'crear_libro.html', {'form': form})


# Vista para crear un nuevo usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')  # Redirige a la lista de usuarios
    else:
        form = UsuarioForm()

    return render(request, 'crear_usuario.html', {'form': form})


# Vista para crear una nueva reseña
def crear_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reviews')  # Redirige a la lista de reseñas
    else:
        form = ReviewForm()

    return render(request, 'crear_review.html', {'form': form})


# Vista para listar todos los libros
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros.html', {'libros': libros})


# Vista para listar todos los usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})


# Vista para listar todas las reseñas
def listar_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'listar_reviews.html', {'reviews':reviews})