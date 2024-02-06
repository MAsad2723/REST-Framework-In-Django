from django.contrib import admin
from api.models import *
# Register your models here.

#Display other information other than only Name
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields=('name',)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position')
    search_fields=('name',)

# Register our models on Admin Page
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.site_title = "CodeWithAsad"
admin.site.site_header = "Code With Asad - Admin Panel"