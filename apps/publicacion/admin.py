from django.contrib import admin
from .models import Publicacion

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
	fields = (
		'titulo',
		'descripcion',
		'image',
		'autor',
		'fecha',
		'estado'
	)

	class Meta:
		model = Publicacion