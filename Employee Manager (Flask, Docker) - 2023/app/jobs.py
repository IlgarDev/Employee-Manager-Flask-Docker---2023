from flask import Blueprint, redirect, render_template, request, url_for
from database import db
from dbModel import Job

jobs = Blueprint("jobs", __name__, static_folder="static", template_folder="template")

@jobs.route("/jobs")
def home():
    all_jobs = Job.query.all()
    return render_template("jobs.html", jobs = all_jobs)


@jobs.route('/insertJob', methods=['POST'])
def insert_job():
    if request.method == 'POST':
        title = request.form['title']
        my_data = Job(title)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('jobs.home'))


@jobs.route('/updateJob', methods=['POST'])
def update_job():
    if request.method == 'POST':
        my_data = Job.query.get(request.form.get('id'))
        my_data.id = request.form['id']
        my_data.title = request.form['title']
        db.session.commit()
        return redirect(url_for('jobs.home'))
    

@jobs.route('/deleteJob', methods = ['POST', 'GET'])    
def delete_job():
    if request.method == 'POST':
        my_data = Job.query.get(request.form.get('id'))
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('jobs.home'))