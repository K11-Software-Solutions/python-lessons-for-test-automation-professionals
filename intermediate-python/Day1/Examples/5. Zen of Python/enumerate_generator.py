numbers=list(range(1,100))

mygen=(item+1 for item in numbers)
while(True):
    try:
        a=next(mygen)
        print(a)
    except StopIteration as error:
        break

numbers=list(range(1,100))

print("\n\n\n")
mygen=(item+1 for item in numbers)

for x in mygen:
    print(x)

