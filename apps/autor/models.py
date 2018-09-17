from django.db import models

class Autor(models.Model):

	nombre = models.CharField(max_length=255)
	nacionalidad = models.CharField(max_length=255)
	biografia = models.TextField()

	def __str__(self):
		return self.nombre