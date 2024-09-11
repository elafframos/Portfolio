from django.db import models

class Nome(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Area", null=True, blank=True)

    def __str__(self):
        return self.name

    
class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nome do Projeto", blank=True, null=True, default='')
    data = models.DateField(blank=True, null=True, verbose_name="Data do Projeto")
    descricao = models.CharField(max_length=500 ,blank=True, null=False, verbose_name="Descrição", help_text='Maximo de caracteres são 500')
    link = models.CharField(max_length=100, blank=True, null=True, verbose_name="Link")
    nome = models.ForeignKey(Nome, on_delete=models.PROTECT, related_name='app_nome', verbose_name='Área', blank=True, null=True)
    python = models.BooleanField(default=False, blank=True, null=False)
    java = models.BooleanField(default=False, blank=True, null=False)
    css = models.BooleanField(default=False, blank=True, null=False)
    html = models.BooleanField(default=False, blank=True, null=False)
    javascript = models.BooleanField(default=False, blank=True, null=False)
    c = models.BooleanField(default=False, blank=True, null=False)
    
    def __str__(self):
        return f"Variável1: {self.variavel1}, Variável2: {self.variavel2}, Variável3: {self.variavel3}"
