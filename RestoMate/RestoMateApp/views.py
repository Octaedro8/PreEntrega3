from django.shortcuts import render
from .models import Menu
from RestoMateApp.forms import MenuFormulario, BuscaMenuForm

def inicio(request):
    return render(request, "RestoMateApp/index.html")

def contacto(request):
    return render(request, "RestoMateApp/contacto.html")

def menu(request):
    return render(request, "RestoMateApp/menu.html")

def locales(request):
    return render(request, "RestoMateApp/locales.html")

def admin(request):
    return render(request, "RestoMateApp/admin")

def form_comun(request):

    if request.method == 'POST':

        menu =  Menu(categoria=request.POST['categoria'],descripcion=request.POST['descripcion'],precio=request.POST['precio'],disponibilidad=request.POST['disponibilidad'])
        menu.save()

        return render(request, "RestoMateApp/index.html")

    return render(request,"RestoMateApp/form_comun.html")

def form_con_api(request):
    if request.method == "POST":
        miFormulario = MenuFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            menu = Menu(categoria=informacion['categoria'],descripcion=informacion['descripcion'],precio=informacion['precio'],disponibilidad=informacion['disponibilidad'])
            menu.save()
            return render(request, "RestoMateApp/index.html")
    else:
        miFormulario = MenuFormulario()

    return render(request, "RestoMateApp/form_con_api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaMenuForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            contacto = Menu.objects.filter(nombre__icontains=informacion["menu"])

            return render(request, "RestoMateApp/resultados_buscar_form.html", {"menu": menu})
    else:
        miFormulario = BuscaMenuForm()

    return render(request, "RestoMateApp/buscar_form_con_api.html", {"miFormulario": miFormulario})

def mostrar_menu(request):

    menu = Menu.objects.all() #trae todos los menu

    contexto= {"menu":menu} 

    return render(request, "RestoMateApp/mostrar_menu.html",contexto)

def clase_22_menu(request, id):

    menu = Menu.objects.get(id=id)
    menu.delete()
 
    # vuelvo al menú
    menu = Menu.objects.all()  # trae todos los menu
 
    contexto = {"descripcion": descripcion}
 
    return render(request, "RestoMateApp/mostrar_menu.html", contexto)

