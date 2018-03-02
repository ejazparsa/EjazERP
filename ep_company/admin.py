from django.contrib import admin
from .models import Company, CompanyDivision, CompanySubDivision


admin.site.register(Company)
admin.site.register(CompanyDivision)
admin.site.register(CompanySubDivision)
