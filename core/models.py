from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    cedula=models.CharField(max_length=10)

    def cedula_valida(dni):
        if len(dni)!=10:
            raise Exception("Longitud incorrecta")
        if int(dni[:2])<1 and int(dni[:2])>15:
            raise Exception("Código de provincia incorrecto")
        return True
    

class Ingreso(models.Model):
    timestamp=models.DateTimeField(auto_now=True )
    motivo=models.CharField(max_length=50)
    placa=models.CharField(blank=True, null=True, max_length=9)
    persona=models.ForeignKey(Persona, on_delete=models.CASCADE)