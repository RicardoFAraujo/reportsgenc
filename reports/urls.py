# reports/urls.py

from django.urls import path
from reports.views import home, report_list, report_detail
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   # path('', views.home, name='home'),
    path ('',views.report_list, name='report_list'),
    path('reports/', views.report_list, name='report_list'),
    path('reports/<int:report_id>/', views.report_detail, name='report_detail'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
