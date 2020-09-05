from django.db import models

class Municipio(models.Model):
    ibge = models.IntegerField() 
    ibge7 = models.IntegerField()
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=128)
    regiao = models.CharField(max_length=15)
    populacao_2010 = models.IntegerField(null=True)
    capital = models.BooleanField()
    validacao = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.municipio, self.uf)

class Mapeamento(models.Model):
    STATUS = (
        (1, 'Público'),
        (2, 'Não público'),
        (3, 'Sem confirmação'),
        )

    TIPOS_ARQUIVOS = (
        (1, 'PDF Texto'),
        (2, 'PDF imagem'),
        (3, 'DOCX'),
        (4, 'HTML'),
        (5, 'TXT'),
        (6, 'Outro formato'),
        )

    municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS)
    data_inicial = models.DateField()
    link_do = models.URLField()
    tipo_arquivo = models.IntegerField(choices=TIPOS_ARQUIVOS)
    navegacao = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.municipio)