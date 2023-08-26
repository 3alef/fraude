from django.db import models
from django.db import models
from datetime import datetime
# Create your models here.

LOCALIDAD = (
        ("1","Resistencia"),
        ("2","Barranqueras"),
        ("3","Fontana"),
        ("5","Pto. Vilelas"),
        ("6","Colonia Benitez"),
        ("7","Margarita Belen")
    )

TARIFA = (
    ("1","00111"),
    ("2","02A21"),
    ("3","00112"),
    ("4","00114")
)

FALLA =(
    ("1","conexion directa sin medidor"),
    ("2","conexion directa con medidor"),
    ("3","bajada pinchada"),
    ("4","neutro aislado"),
    ("5","bornera quemada"),
    ("6","sin precintos"),
    ("7","precintos cortados"),
    ("8","sin neutro"),
    ("9","medidor tumbado"),
    ("10","display apagado"),
    ("11","para normalizar"),
    ("12","medidor con agua"),
    ("13","puente entre fase"),
    ("14","carcasa rota"),
    ("15","conexion invertida"),
    ("16","medidor quemado"),
    ("17","medidor adulterado"),
    ("18","medidor frenado"),
    ("19","medidor parado"),
    ("20","integrador defasado")
)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nro_cliente= models.PositiveBigIntegerField(default=0)
    nombre_apellido = models.CharField(max_length=30,default=False)
   

    class Meta:
        verbose_name_plural='Clientes'


    def __str__(self):
        fila = str(self.nro_cliente)+"-" + self.nombre_apellido
        return fila


class Suministro(models.Model):    
    id_suministro = models.AutoField(primary_key=True)
    numero_suministro= models.SmallIntegerField(default=1)
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    direccion = models.CharField(max_length=40)
    nro_medidor= models.PositiveIntegerField()
    ruta= models.PositiveBigIntegerField()
    localidad = models.CharField(max_length=1, choices= LOCALIDAD, default="1")
    tarifa = models.CharField(max_length=1, choices=TARIFA, default="1")

    class Meta:
        verbose_name_plural='Suministros'

    def __str__(self):
        fila = str(self.numero_suministro) + self.direccion
        return fila
    

class Trabajo(models.Model):
    id_trabajo=models.AutoField(primary_key=True)
    fecha = models.DateField()
    cliente= models.ForeignKey('Cliente', on_delete=models.CASCADE)
    falla= models.ForeignKey('Falla', on_delete=models.CASCADE)
    pago= models.ForeignKey('Pago',on_delete=models.CASCADE,blank=True,default="")
    observacion= models.CharField(max_length=150,blank =True,default="")
    
    class Meta:
        verbose_name_plural='Trabajos'

    
    def __str__(self):
        fila = str(self.fecha)+"-"+str(self.cliente)+"-"+ str(self.falla) + self.observacion
        return fila


class Falla(models.Model):
    id_falla= models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length= 2, choices=FALLA, default="1")


    class Meta:
        verbose_name_plural='Fallas'


    def __str__(self):
        return self.descripcion


class Pago(models.Model):
    id_pago= models.AutoField(primary_key=True,blank=True)
    nro_recibo= models.PositiveBigIntegerField()
    fecha_pago=models.DateField()
    monto=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.nro_recibo)