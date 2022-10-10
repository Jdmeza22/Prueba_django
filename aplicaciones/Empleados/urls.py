from . import views
from django.urls import path,include

urlpatterns =[
    path('',views.home),
    path('login/',views.login_request,name='login'),
    path('registrarEmpleado/',views.registrarEmpleado),
    path('edicionEmpleado/<cedula>',views.edicionEmpleado),
    path('editarEmpleado/',views.editarEmpleado),
    path('eliminarEmpleado/<cedula>',views.eliminarEmpleado)
    
]