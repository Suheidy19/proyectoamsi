from django.db import models

# Create your models here.
class Provider(models.Model):
    firstname = models.CharField(max_length=80, verbose_name='Nombre:')
    lastname = models.CharField(max_length=80, verbose_name='Apellidos')
    address = models.CharField(max_length=250, verbose_name='Dirección')
    phone = models.CharField(max_length=15, verbose_name='Teléfono')
    email = models.EmailField(max_length=100, verbose_name='Correo electrónico')

    def __str__(self):
        return "{0} {1}".format(self.firstname, self.lastname)

    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural= 'Proveedores'



class Clients(models.Model):
    firstname = models.CharField(max_length=80, verbose_name='Nombre:')
    lastname = models.CharField(max_length=80, verbose_name='Apellidos')
    address = models.CharField(max_length=250, verbose_name='Dirección')
    phone = models.CharField(max_length=15, verbose_name='Teléfono')
    email = models.EmailField(max_length=100, verbose_name='Correo electrónico')
    
    def __str__(self):
        return "{0} {1}".format(self.firstname, self.lastname)

    class Meta:
        verbose_name= 'Cliente'
        verbose_name_plural= 'Clientes'

class Products(models.Model):
    Name = models.CharField(max_length=80, verbose_name='Nombre:')
    Price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='Precio')
    Brand = models.CharField(max_length=200, verbose_name='Marca')
    Expiration_date = models.CharField(max_length=50, verbose_name='Fecha de caducidad')


    def __str__(self):
        return "{0} {1} -- ${2}".format(self.Name, self.Brand,self.Price)

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'


"""
class ProductsFK(models.Model):
    Name = models.ForeignKey(Products, related_name='Name')
    Price = models.ForeignKey(Products, related_name='Price')
"""



class Sales(models.Model):
    Name_Clients=models.ForeignKey(Clients,on_delete=models.CASCADE, verbose_name='Nombre Cliente')
    Date = models.CharField(max_length=20, verbose_name='Fecha de Venta')
    # Name_Products=models.CharField(Products, related_name='Name', verbose_name='Nombre del producto')
    # Price_Products=models.CharField(Products, related_name='Price', verbose_name='Precio del producto')
    Total = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='Total de la venta')
    Discount =models.CharField(max_length=20, verbose_name='Descuento')


    def __str__(self):
        return "{0}--${1}--${2}".format(self.Name_Clients,self.Date,self.Total)

    class Meta:
        verbose_name= 'Venta'
        verbose_name_plural= 'Ventas'


class Invoices(models.Model):
    Name_Clients=models.ForeignKey(Clients,on_delete=models.CASCADE, verbose_name='Nombre Cliente')
    Date = models.DateField(verbose_name='Fecha de factura')
    # ID_Sales=models.ForeignKey(Clients,on_delete=models.CASCADE, verbose_name='Nombre Cliente')
    Total = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='Total de la venta')
   

    def __str__(self):
        return "{0}--${1}--${2}".format(self.Name_Clients,self.Date,self.Total)

    class Meta:
        verbose_name= 'Factura'
        verbose_name_plural= 'Facturas'

 