def FuncA(a, b):
    result=0
    err=True
    try:  
        #assert(b != 0)
        result=a/b
    except ZeroDivisionError as e:
        err=False
        result = 'Division by zero not allowed'
    return result, err

answer, ok=FuncA(10, 0)
if(ok):
    print(answer)
else:
    print("Error: " + answer)

