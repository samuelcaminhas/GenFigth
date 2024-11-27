from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date
from .models import Aluno, Pagamento

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard(request):
    total_alunos = Aluno.objects.count()
    pagamentos_mes = Pagamento.objects.filter(data_pagamento__month=date.today().month).count()
    alunos_atrasados = Aluno.objects.filter(mensalidade_em_dia=False).count()

    context = {
        'total_alunos': total_alunos,
        'pagamentos_mes': pagamentos_mes,
        'alunos_atrasados': alunos_atrasados,
    }
    return render(request, 'core/dashboard.html', context)
