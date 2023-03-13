from flask import Flask, render_template
from dbModel import Employee, Job
from jobs import jobs;
from employees import employees;
from database import db

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = "magicKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/employeesdb'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)
app.register_blueprint(jobs, url_prefix="")
app.register_blueprint(employees, url_prefix="")

@app.route("/")
def home():
    all_data = Employee.query.all()
    for data in all_data:
        data.job = Job.query.filter_by(id = data.job_id).first()
    all_jobs = Job.query.all()
    return render_template("index.html", employees = all_data, jobs = all_jobs)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')