from django.db import models

class Personagem(models.Model):
    # id é criado automaticamente 
    nome = models.CharField(max_length=100)
    afiliacao = models.CharField(max_length=255, blank=True)
    aliados = models.TextField(blank=True)
    inimigos = models.TextField(blank=True)

    def __str__(self):
        return self.nome
