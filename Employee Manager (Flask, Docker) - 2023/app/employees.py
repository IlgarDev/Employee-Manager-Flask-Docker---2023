from flask import Blueprint, redirect, render_template, request, url_for
from database import db
from dbModel import Employee, Job

employees = Blueprint("employees", __name__, static_folder="static", template_folder="template")

@employees.route('/employees')
def home():
    all_data = Employee.query.all()
    for data in all_data:
        data.job = Job.query.filter_by(id = data.job_id).first()
    return render_template("employees.html", employees = all_data)

@employees.route('/insert', methods=['POST'])
def insert_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        job = Job.query.filter_by(title = request.form['job']).first()
        my_data = Employee(name, email, phone, job.id)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('employees.home'))

@employees.route('/update', methods = ['POST'])
def update_employee():
    if request.method == 'POST':
        my_data = Employee.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        my_data.job_id = Job.query.filter_by(title = request.form['job']).first()
        my_data.job_id = my_data.job_id.id
        db.session.commit()
        return redirect(url_for('employees.home'))

@employees.route('/delete', methods = ['POST', 'GET'])    
def delete_employee():
    if request.method == 'POST':
        my_data = Employee.query.get(request.form.get('id'))
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('employees.home'))
