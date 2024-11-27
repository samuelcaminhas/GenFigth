from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    contato_emergencia = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    data_matricula = models.DateField(auto_now_add=True)
    mensalidade_em_dia = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data_vencimento = models.DateField()

    def __str__(self):
        return f"Pagamento de {self.aluno.nome} - {self.data_pagamento}"
