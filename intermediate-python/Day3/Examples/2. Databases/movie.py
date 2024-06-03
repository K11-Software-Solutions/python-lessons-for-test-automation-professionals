import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

conn = sa.create_engine("sqlite:///movie.db")

theBase = declarative_base()

def get_connection():
    return theBase,conn

class Product(theBase):
    __tablename__ = 'products'
    id= sa.Column(sa.Integer, primary_key=True)
    title= sa.Column('title', sa.String(32))
    in_stock= sa.Column('in_stock', sa.Boolean)
    quantity= sa.Column('quantity', sa.Integer)
    price= sa.Column('price', sa.Numeric)