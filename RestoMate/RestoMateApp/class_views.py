from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Menu, Locales, Contacto
from django.urls import reverse_lazy

class MenuListView(ListView):
    model = Menu
    template_name = "RestoMateApp/class_list_menu.html"

class LocalesListView(ListView):
    model = Locales
    template_name = "RestoMateApp/class_list_locales.html"

class ContactoListView(ListView):
    model = Contacto
    template_name = "RestoMateApp/class_list_contacto.html"

class MenuDetailView(DetailView):
    model = Menu
    template_name = "RestoMateApp/class_detail.html"


class MenuCreateView(CreateView):
    """
    Esta clase envía por defecto un formulario al archivo html. Envía los campos indicados en la lista "fields" y podemos hacer uso de dicho formulario bajo la key "form".
    """

    model = Menu
    template_name = "RestoMateApp/class_create.html"
    fields = ["categoria", "descripcion", "precio", "disponible"]

    # En success_url indicamos la vista que queremos visitar una vez que se genera un item del menu con éxito. Lo podemos hacer de 2 formas:
    
    # Indicando la URL
    # success_url = "../class-list/"
    # Con el reverse_lazy indicamos el nombre de la vista
    success_url = reverse_lazy("Menu")


class MenuUpdateView(UpdateView):
    model = Menu
    success_url = reverse_lazy("List")
    fields = ["id", "categoria", "descipcion", "precio", "disponibilidad"]
    template_name = "RestoMateApp/class_update.html"


class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy("List")
    template_name = 'RestoMateApp/class_confirm_delete.html'

