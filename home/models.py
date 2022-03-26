from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=15)
    status = models.CharField(
        max_length=1,
        choices=(
            ('A', 'Ativo'),
            ('B', "Bloqueado"),
            ('C', 'Cancelado'),
        )
    )

    def __str__(self):
        return self.nome


class Curso(models.Model):
    curso = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    status = models.CharField(
        max_length=100,
        choices=(
            ('A', 'Ativo'),
            ('I', "Inativo"),
        )
    )

    def __str__(self):
        return self.curso
