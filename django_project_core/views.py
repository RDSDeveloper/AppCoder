from django.http import HttpResponse
import datetime
from django.template import Context, Template, loader


def first_hello(request):
    return HttpResponse("My first hello")


def second_hello(request):
    return HttpResponse("My second hello")


def today(request):
    today = datetime.datetime.now()
    return HttpResponse(f"Now is {today}")


def name(request, name):
    return HttpResponse(f"My name is {name}")


def testing_template(self):
    nombre = "Rodri"
    apellido = "Santos"
    lista_notas = [1, 2, 4, 5, 6, 3, 5]
    diccionario = {"nombre": nombre, "apellido": apellido, "lista_notas": lista_notas}
    
    
    # html = open("template.html")
    # open_html = Template(html.read())
    # html.close()
    # my_context = Context(diccionario)
    
    

    template_loader = loader.get_template("template.html")
    template_rendering = template_loader.render(diccionario)

    return HttpResponse(template_rendering)
