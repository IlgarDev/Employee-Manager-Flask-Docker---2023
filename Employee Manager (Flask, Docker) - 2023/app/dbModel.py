from database import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    
    def __init__(self, title):
        self.title = title


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))

    def __init__(self, name, email, phone, job_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.job_id = job_id