from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
        else:
            print(form.errors)
    else:
        form = EmployeeForm()

    return render(request, 'index.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    return render(request, 'edit.html', {'form': form, 'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, request.FILES, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('show')
    return render(request, 'edit.html', {'form': form, 'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('show')
