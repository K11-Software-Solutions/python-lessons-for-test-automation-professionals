def foo(a, b, c, d, e):
        print(a, b, c, d, e)
        
mydict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
mylist = [10, 20, 30, 40, 50]
myset = set("Hello!")
mylist2 = [10, 20, 30]
mylist3 = [40, 50]

foo(*mydict)
foo(**mydict)
foo(*mylist)
foo(*myset)
foo(*mylist2, *mylist3)
