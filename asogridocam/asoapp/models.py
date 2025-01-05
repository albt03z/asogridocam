from django.db import models

# Create your models here.
class Country(models.Model):
    """Clase que representa un país."""
    name = models.CharField(max_length=100, verbose_name='Nombre del país')
    alpha2_code = models.CharField(max_length=2, primary_key=True, verbose_name='Código del país')
    alpha3_code = models.CharField(max_length=3, verbose_name='Código del país (3 letras)')
    flag = models.URLField(max_length=200, null=True, verbose_name='URL de la bandera')
    
    class Meta:
        db_table = 'countries'
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name

class Clients(models.Model):
    """Clase que representa un cliente en la base de datos."""
    name = models.CharField(max_length=40, verbose_name='Nombre del cliente')
    surname = models.CharField(max_length=40, verbose_name='Apellido del cliente')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Correo electrónico')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Número de teléfono')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='País de residencia')
    message = models.TextField(verbose_name='Mensaje')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        db_table = 'clients'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    from django.db import models

class Subscriber(models.Model):
    """Modelo para los suscriptores del boletín."""
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de suscripción')

    class Meta:
        db_table = 'subscribers'
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email