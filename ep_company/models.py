from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=256, verbose_name='Company Name')
    location = models.CharField(max_length=128, verbose_name='Location', blank=True)
    description = models.TextField(max_length=2000, verbose_name='Description', blank=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'About Company'

    def __str__(self):
        return self.company_name


class CompanyDivision(models.Model):
    name_division = models.CharField(max_length=256, verbose_name='Division Name')
    company = models.ForeignKey(Company, verbose_name='Company', on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, verbose_name='Description', blank=True)

    class Meta:
        verbose_name = 'Company Division'
        verbose_name_plural = 'About Division'

    def __str__(self):
        return self.name_division


class CompanySubDivision(models.Model):
    sub_division_name = models.CharField(max_length=256, verbose_name='Sub Division')
    division_name = models.ForeignKey(CompanyDivision, verbose_name='Division', on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, verbose_name='Description', blank=True)

    class Meta:
        verbose_name = 'Sub Division'
        verbose_name_plural = 'About Sub Division'

    def __str__(self):
        return self.sub_division_name