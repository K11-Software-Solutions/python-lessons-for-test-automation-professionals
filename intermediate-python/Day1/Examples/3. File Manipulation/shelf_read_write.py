import shelve

cast = shelve.open("./code/movie")
cast["bob"]="Robert Culp"
cast["ted"]="Elliot Gould"
cast["carol"]="Natalie Wood"
cast["alice"]="Dyan Cannon"
cast.close()

#exception because shelf closed
#cast["alice"]="supported" 

cast=shelve.open("./code/movie")
print(dict(cast))
