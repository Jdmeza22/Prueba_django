from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH
from django.db import models

class Trabajadores(models.Model):
    nombre = models.CharField(max_length=20)
    cedula = models.IntegerField(primary_key=True)
    numero_Celular = models.IntegerField()
    fecha_Nacimiento = models.DateField()
    correo = models.EmailField()
    
    def __str__(self):
        texto ="{0} ({1})"
        return texto.format(self.nombre,self.cedula)