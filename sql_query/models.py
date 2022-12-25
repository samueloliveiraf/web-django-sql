from django.db import models


class SqlQuery(models.Model):
    nome = models.CharField(max_length=512, help_text='Nome completo')
    idade = models.CharField(max_length=512, help_text='Idade')
    profissao = models.CharField(max_length=512, help_text='Profissão')
    jogo_preferido = models.CharField(max_length=512, help_text='Seu jogo preferido')
    id_usuario = models.CharField(max_length=512)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'sql_query'
