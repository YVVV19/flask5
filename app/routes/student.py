from . import app
from db import Student, Config, Group 
from sqlalchemy import select, update, delete
from flask import jsonify


app.get("/students")
def student_list():
    with Config.SESSION() as session:
        query = select(Student)
        data = session.scalars(query).all()

        result = jsonify([{"name":item.name} for item in data])
        return result