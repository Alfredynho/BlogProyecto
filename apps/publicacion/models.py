from django.db import models
from apps.autor.models import Autor

class Publicacion(models.Model):

	titulo = models.CharField(max_length=255)
	descripcion = models.TextField()
	image = models.ImageField(upload_to = "imagenes/publicaciones")
	autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
	fecha = models.DateTimeField()
	estado = models.BooleanField(default = True)

	def __str__(self):
		return self.titulo
