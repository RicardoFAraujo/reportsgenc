# reports/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Report
from collections import defaultdict
from itertools import groupby
from operator import attrgetter
def home(request):
    return render(request, 'home.html')

@login_required
def report_list(request):
    if request.user.is_superuser:  # Verifica se o usuário é um superusuário
        reports = Report.objects.all().order_by('company__name')  # Ordena por empresa
    else:
        if hasattr(request.user, 'userprofile') and request.user.userprofile.company:
            reports = Report.objects.filter(company=request.user.userprofile.company).order_by('company__name')
        else:
            reports = Report.objects.none()

    # Agora, vamos agrupar os relatórios por empresa
    reports_by_company = {}
    for company, group in groupby(reports, key=attrgetter('company')):
        reports_by_company[company] = list(group)
    
    print(f"Reports by company: {reports_by_company}")
    return render(request, 'reports/report_list.html', {'reports_by_company': reports_by_company})

@login_required
def report_detail(request, report_id):
    if request.user.is_superuser:  # Verifica se o usuário é um superusuário
        report = get_object_or_404(Report, id=report_id)  # Permite acesso a qualquer relatório
    else:
        report = get_object_or_404(Report, id=report_id, company=request.user.userprofile.company)  # Restringe ao relatório da empresa do usuário

    return render(request, 'reports/report_detail.html', {'report': report})


