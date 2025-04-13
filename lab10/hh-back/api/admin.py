from django.contrib import admin
from .models import Company,Vacancy
# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=('id','name','city','address','user')
    search_fields=('id','name','city','address','user')

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display=('id','name','salary')
    search_fields=('id','name','salary')