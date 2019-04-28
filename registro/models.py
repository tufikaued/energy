from django.db import models

# Create your models here.
class RegistroEnergia(models.Model):
    """
    Clase para registrar el consumo de energia
    """
    consumo_kwatts = models.PositiveIntegerField(help_text="Kilowatts consumidos indicador 1.8")
    generado_kwatts = models.PositiveIntegerField(help_text="Kilowatts generados indicador 2.8")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de creacion")
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")

    class Meta:
        verbose_name = 'registro_energia'
        verbose_name_plural = 'registros_energia'

    def __str__(self):
        """
        representa el objeto RegistroEnergia
        """
        return "consumido: {0} / generado: {1}".format(self.consumo_kwatts, self.generado_kwatts)


