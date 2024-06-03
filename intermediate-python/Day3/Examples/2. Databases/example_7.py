import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

conn = sa.create_engine("sqlite:///movie.db")

theBase = declarative_base()

def get_connection():
    return theBase,conn

class Movie(theBase):
    __tablename__="Actors"
    role=sa.Column("role", sa.String, primary_key=True)
    name=sa.Column("name", sa.String)
    age=sa.Column("age", sa.Integer)

    def __init__(self, role, name, age):
        self.role=role
        self.name=name
        self.age=age

    def __repr__ (self):
        return "<Actors({}, {})>" \
               .format(self.name, self.age)

class Product(Base):
    __tablename__ = 'products'
    id=Column(Integer, primary_key=True)
    title=Column('title', String(32))
    in_stock=Column('in_stock', Boolean)
    quantity=Column('quantity', Integer)
    price=Column('price', Numeric)