from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import PublicacionForm
from .models import Publicacion

def publicacion(request):

	lista_publicacion = Publicacion.objects.all()
	mensaje = "Bienvenido a mi Blog"

	return render(request,'publicaciones.html',
		{
			'lista_publicacion':lista_publicacion,
			'mensaje':mensaje
		}
		)


class CreatePostView(CreateView):
	model = Publicacion
	form_class = PublicacionForm
	template_name = "crear_publicacion.html"
	success_url = "/publicaciones"