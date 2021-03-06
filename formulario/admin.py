from django.contrib import admin

from formulario.models import Municipio, Mapeamento


class MunicipioAdmin(admin.ModelAdmin):
    fields = ('ibge', 'ibge7', 'municipio', 'uf', 'regiao', 'populacao_2010', 'capital')
    readonly_fields = ('ibge', 'ibge7', 'municipio', 'uf', 'regiao', 'populacao_2010', 'capital')

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super(MunicipioAdmin, self).get_queryset(request)
        return qs.order_by('municipio')

class MapeamentoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MapeamentoAdmin, self).get_queryset(request)
        return qs.filter(validacao=False)

admin.site.register(Mapeamento, MapeamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
