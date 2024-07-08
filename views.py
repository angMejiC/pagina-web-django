from django.shortcuts import render
from .models import TopoWeb_usuario



def quienes_somos(request):
    return render(request, 'quienes_somos.html')


def nuestros_servicios(request):
    return render(request, "front.html")

def pagina_principal(request):
    formulario_procesado = False
    if request.method == 'POST':
        # Procesar el formulario si se ha enviado una solicitud POST
        nombre = request.POST.get('nombre')
        correo = request.POST.get('email')
        nota = request.POST.get('mensaje')

        # Crear una instancia del modelo Usuario con los datos del formulario
        usuario = TopoWeb_usuario(nombre=nombre, email=correo, mensaje=nota)
        usuario.save()

        # Establecer formulario_procesado a True
        formulario_procesado = True


       # Si la solicitud no es POST o el formulario no se ha procesado, simplemente renderizar el formulario
    return render(request, 'front.html', {'formulario_procesado': formulario_procesado})
        # Renderizar una plantilla de confirmación