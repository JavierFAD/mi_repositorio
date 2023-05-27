from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola mundo!, Hola Que onda!?")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a la página")

def probando_template(request):
    mi_html = open('./Clase_17/plantillas/index.html')
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)