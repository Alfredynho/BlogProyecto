from django.contrib import admin
from .models import Autor

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
	fields = (
		'nombre',
		'nacionalidad',
		'biografia'
		)

	class Meta:
		model = Autor