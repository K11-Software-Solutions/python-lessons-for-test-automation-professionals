def decorator1(func):
    if func:
        print(f"registering {func.__name__} with decorator1")
    else:
        print('decorator1')
    return func

def decorator2(func):
    if func:
        print(f"registering {func.__name__} with decorator2")
    else:
        print('decorator2')
    return func


@decorator1  # decorate def decorator2(func)
@decorator2  # decorate def Func1()
def Func1():
    print("func")

Func1()
