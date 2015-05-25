from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from todoapp import app

db = SQLAlchemy(app)

class Todo (db.Model):
    __tablename__ = "todo"
    id = db.Column('id', db.Integer, primary_key=True)
    category_id = db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
    priority_id = db.Column('priority_id', db.Integer, db.ForeignKey('priority.id'))
    description = db.Column('description', db.Unicode)
    creation_date = db.Column('creation_date', db.Date)
    is_done = db.Column('is_done', db.Boolean)

    priority = db.relationship('Priority', foreign_keys=priority_id)
    category = db.relationship('Category', foreign_keys=category_id)

    def __init__(self, category, priority, description):
        self.category = category
        self.priority = priority
        self.description = description
        self.creation_date = datetime.utcnow()
        self.is_done = False

class Priority (db.Model):
    __tablename__ = "priority"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    value = db.Column('value', db.Integer)

class Category (db.Model):
    __tablename__ = "category"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
