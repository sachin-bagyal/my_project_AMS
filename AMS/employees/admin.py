from django.contrib import admin
from employees.models import employees
# Register your models here.
class employeesAdmin(admin.ModelAdmin):
    list_display = ('emp_id','emp_name','emp_email','emp_phone_no','emp_doj','emp_dob','emp_job_title','emp_address')

admin.site.register(employees,employeesAdmin)
