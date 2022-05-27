from datetime import datetime

from appf import db


class Equip(db.Model):
    __tablename__ = 'equips'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    type_id = db.Column(db.Integer(), db.ForeignKey('types_eq.id'))
    manufacturer_id = db.Column(db.Integer(), db.ForeignKey('manufacturers.id'))

    def __repr__(self):
        return f'<{{self.id}}:{{self.name[:50]}}>'

class Type_eq(db.Model):
    __tablename__ = 'types_eq'
    id = db.Column(db.Integer(), primary_key = True)    
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    equips = db.relationship('Equip', backref = 'type_eq')

    def __repr__(self):
        return f'<{{self.id}}:{{self.name}}>'

class Manufacturer(db.Model):
    __tablename__ ='manufacturers'
    id = db.Column(db.Integer(), primary_key = True)    
    short_name = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(300), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    equips = db.relationship('Equip', backref = 'manufacturer')

    def __repr__(self):
        return f'<{{self.id}}:{{self.short_name}}>'

# db.create_all()



