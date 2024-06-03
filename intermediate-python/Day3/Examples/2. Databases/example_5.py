from movie import Movie, get_connection
from sqlalchemy.orm import sessionmaker

the_base,conn = get_connection()

the_base.metadata.create_all(conn)


first=Movie("Bob", "Robert Culp", 79)
second=Movie("Ted", "Elliot Gould", 79)
third=Movie("Carol", "Natalie Wood", 43)
fourth=Movie("Alice", "Dyan Cannon", 81)

print(first)

session=sessionmaker(bind=conn) 
theSession=session()
theSession.add(first)
theSession.add_all([second, third, fourth])
theSession.commit()
