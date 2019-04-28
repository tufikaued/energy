from django.contrib import admin
from .models import RegistroEnergia

# Register your models here.
class RegistroEnergiaManager(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at', 'id']
    list_display    = ['consumo_kwatts', 'generado_kwatts']
    search_fields   = ['consumo_kwatts', 'generado_kwatts',]

admin.site.register(RegistroEnergia, RegistroEnergiaManager)
