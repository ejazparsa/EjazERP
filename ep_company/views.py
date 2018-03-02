from django.shortcuts import render, get_object_or_404
from .models import Company, CompanyDivision


def list_company(request):
    companys = Company.objects.all()
    return render(request, 'ep_company/list_company.html', {'companys':companys})

def list_division(request):
    divisions = CompanyDivision.objects.all()
    return render(request, 'ep_company/list_division.html', {'divisions':divisions})

def division_detail(request, pk):
    div_detail = get_object_or_404(CompanyDivision, pk=pk)
    return render(request, 'ep_company/division_detail.html', {'item':div_detail})

