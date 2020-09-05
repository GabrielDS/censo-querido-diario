from django.contrib import admin

from formulario.models import Municipio, Mapeamento


class MunicipioAdmin(admin.ModelAdmin):
    fields = ('ibge', 'ibge7', 'municipio', 'uf', 'regiao', 'populacao_2010', 'capital', 'validacao')
    readonly_fields = ('ibge', 'ibge7', 'municipio', 'uf', 'regiao', 'populacao_2010', 'capital')

class MapeamentoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MapeamentoAdmin, self).get_queryset(request)
        return qs.filter(municipio__validacao=False)

admin.site.register(Mapeamento, MapeamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
