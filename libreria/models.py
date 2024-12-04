from django.db import models
class Libro(models.Model):
    idlibro = models.AutoField(primary_key=True)  # Campo autoincremental para IdLibro
    nombre = models.CharField(max_length=255)    # Campo para el nombre del libro
    autor = models.CharField(max_length=255)     # Campo para el autor del libro
    publicacion = models.DateField()             # Fecha de publicación

    def _str_(self):
        return self.nombre


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)  # Campo autoincremental para IdUsuario
    nombre = models.CharField(max_length=255)       # Campo para el nombre del usuario
    contraseña = models.CharField(max_length=255)   # Campo para la contraseña

    def _str_(self):
        return self.nombre


class Review(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)  # Relación con Libro
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relación con Usuario
    contenido = models.TextField()  # Campo para el contenido de la reseña

    def _str_(self):
        return f'Review de {self.usuario.nombre} para {self.libro.nombre}'