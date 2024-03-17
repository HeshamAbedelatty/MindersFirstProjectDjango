from django.shortcuts import render

# Create your views here.
from .models import Employee

def show_all_employees(request):
    employees = Employee.objects.all() # query get all records in table employee
    # context = {
    #     'employees': employees
    # }
    return render(request, 'index.html', {'employees': employees})


# def insert_employee(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Employee inserted successfully.')
#             return redirect('insert_employee')  # Redirect to the same page after successful submission
#     else:
#         form = EmployeeForm()
#     return render(request, 'insert_employee.html', {'form': form})