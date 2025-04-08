from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import Employee
from . import db
from .forms import EmployeeForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@main.route('/add', methods=['GET', 'POST'])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        new_employee = Employee(
            name=form.name.data,
            department=form.department.data,
            email=form.email.data,
            salary=form.salary.data
        )
        db.session.add(new_employee)
        db.session.commit()
        flash('Employee added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_employee.html', form=form)

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get_or_404(id)
    form = EmployeeForm(obj=employee)
    if form.validate_on_submit():
        employee.name = form.name.data
        employee.department = form.department.data
        employee.email = form.email.data
        employee.salary = form.salary.data
        db.session.commit()
        flash('Employee updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('edit_employee.html', form=form, employee=employee)

@main.route('/delete/<int:id>')
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    flash('Employee deleted successfully!', 'success')
    return redirect(url_for('main.index'))
