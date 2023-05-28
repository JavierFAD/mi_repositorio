from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime as dt
from django.template import loader
from AppCoder.models import Curso

def probandoTemplate(self):
    
    nom = "Javier"
    ape = "Acosta"
    listaDeNotas = [2, 2, 3, 7, 5, 2]
    
    diccionario = {"nombre":nom, "apellido":ape, "hoy": str(dt.now()), "notas": listaDeNotas}
    #
    #miHtml = open(".\Coder\Plantillas\index.html")
    #
    #plantilla = Template(miHtml.read())
    #
    #miHtml.close()
    #
    #miContexto = Context(diccionario)
    
    plantilla = loader.get_template("index.html")
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)

def curso(self):
    curso = Curso(nombre="Desarrollo web", camada= "19881")
    curso.save()
    documentoDeTexto = f"---->Curso: {curso.nombre}    Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)
