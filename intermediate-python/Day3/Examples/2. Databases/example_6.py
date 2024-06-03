from movie import get_connection, Movie 
from sqlalchemy.orm import sessionmaker

the_base,conn = get_connection()
the_base.metadata.bind = conn

session=sessionmaker()
session.bind=conn
theBase=session()

movies = theBase.query(Movie).all()
print(movies)

actor=theBase.query(Movie).first()
print(actor)

