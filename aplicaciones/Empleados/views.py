from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from aplicaciones import Empleados
from .models import Trabajadores


def login_request(request):
    if request.method == "POST":
       form =AuthenticationForm(request,data=request.POST)
       if form.is_valid():
           usuario = form.cleaned_data.get('username')
           contraseña = form.cleaned_data.get('password')
           user = authenticate(username=usuario, password=contraseña)
           if user is not None: 
                login(request,user)
                messages.info(request,f"Estas logeado")
                return redirect('/')
           else:
                messages.info(request,f"Usuario y/o contraseña incorrecta")
       else:
                messages.info(request,f"Usuario y/o contraseña incorrecta")
    form = AuthenticationForm()
    return render(request,'login.html',{"form":form})

def home(request):
    listaTrabajadores =Trabajadores.objects.all()
    return render (request,"gestionEmpleados.html",{"trabajadores":listaTrabajadores})

def registrarEmpleado(request):
    cedula =request.POST['txtcedula']
    nombre =request.POST['txtnombre']
    numero_Celular =request.POST['txtnumero_Celular']
    fecha_Nacimiento =request.POST['txtfecha_Nacimiento']
    correo =request.POST['txtcorreo']

    trabajadores = Trabajadores.objects.create(
    cedula=cedula,nombre=nombre,numero_Celular=numero_Celular,fecha_Nacimiento=fecha_Nacimiento,correo=correo)
    messages.success(request,'¡Empleado registrado con exito!')
    return redirect('/')

def edicionEmpleado(request,cedula):
    trabajadores = Trabajadores.objects.get(cedula=cedula)
    return render (request,"edicionEmpleado.html",{"trabajadores":trabajadores})

def editarEmpleado(request):
    cedula =request.POST['txtcedula']
    nombre =request.POST['txtnombre']
    numero_Celular =request.POST['txtnumero_Celular']
    fecha_Nacimiento =request.POST['txtfecha_Nacimiento']
    correo =request.POST['txtcorreo']

    trabajadores = Trabajadores.objects.get(cedula=cedula)
    trabajadores.nombre = nombre
    trabajadores.numero_Celular = numero_Celular
    trabajadores.fecha_Nacimiento = fecha_Nacimiento
    trabajadores.correo = correo
    trabajadores.save()
    messages.success(request,'¡Lista de empleados actualizada!')
    
    return redirect('/')

def eliminarEmpleado(request,cedula):
    trabajadores = Trabajadores.objects.get(cedula=cedula)
    trabajadores.delete()
    messages.success(request,'¡Empleado eliminado!')
    return redirect('/')