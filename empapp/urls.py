from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.employeeFormPage, name='employeeFormPage'),      # GET  /employee/
    path('create/', views.createEmployee,   name='createEmployee'),
    path('update/<int:employee_id>/', views.updateEmployee, name='updateEmployee'),  # POST /employee/update/{id},
     path('delete/<int:employee_id>/', views.deleteEmployee, name='delete_employee'),
     path('employees/', views.get_employees, name='get_employees')
]
