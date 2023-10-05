"""
URL configuration for RestoMate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from RestoMateApp import views
from RestoMateApp import class_views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('menu/', views.menu, name="Menu"),
    path('locales/', views.locales, name="Locales"),
    path('contacto/', views.contacto, name="Contacto"),
    path('form-comun/', views.form_comun, name="Form-Comun"),
    path('form-con-api/', views.form_con_api, name="Form-Con-Api"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar-Form-Con-Api"),
    path('mostrar-menu/', views.mostrar_menu, name="Mostrar_Menu"),
    path('confirmar-borrado-menu/<id>/', views.clase_22_menu),
    path('admin/', views.admin, name="Admin")
]

# URL's basadas en clases
urlpatterns += [
    path('class-list/', class_views.MenuListView.as_view(), name="List"),
    path('class-list-menu/', class_views.MenuListView.as_view(), name="Ver_Menu"),
    path('class-list-locales/', class_views.LocalesListView.as_view(), name="Ver_Locales"),
    path('class-list-contacto/', class_views.ContactoListView.as_view(), name="Ver_Contacto"),    
    path('class-detail/<pk>/', class_views.MenuDetailView.as_view(), name="Detail"),
    path('class-create/', class_views.MenuCreateView.as_view(), name="Create"),
    path('class-update/<pk>/', class_views.MenuUpdateView.as_view(), name="Update"),
    path('class-delete/<pk>/', class_views.MenuDeleteView.as_view(), name="Delete"),
]
# objects.get(pk=pk)

