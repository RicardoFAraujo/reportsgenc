# reports/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Report
from collections import defaultdict
def home(request):
    return render(request, 'home.html')

@login_required
def report_list(request):
    if request.user.is_superuser:  # Verifica se o usuário é um superusuário
        reports = Report.objects.all()  # Exibe todos os relatórios
    else:
        # Verifica se o usuário tem um perfil e se está associado a uma empresa
        if hasattr(request.user, 'userprofile') and request.user.userprofile.company:
            reports = Report.objects.filter(company=request.user.userprofile.company)  # Exibe apenas os relatórios da empresa do usuário
        else:
            reports = Report.objects.none()  # Se não tiver perfil ou empresa, não mostra nada

    return render(request, 'reports/report_list.html', {'reports': reports})

@login_required
def report_detail(request, report_id):
    if request.user.is_superuser:  # Verifica se o usuário é um superusuário
        report = get_object_or_404(Report, id=report_id)  # Permite acesso a qualquer relatório
    else:
        report = get_object_or_404(Report, id=report_id, company=request.user.userprofile.company)  # Restringe ao relatório da empresa do usuário

    return render(request, 'reports/report_detail.html', {'report': report})


