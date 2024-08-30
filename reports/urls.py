# reports/urls.py

from django.urls import path
from reports.views import home, report_list, report_detail
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reports/', views.report_list, name='report_list'),
    path('reports/<int:report_id>/', views.report_detail, name='report_detail'),
]
