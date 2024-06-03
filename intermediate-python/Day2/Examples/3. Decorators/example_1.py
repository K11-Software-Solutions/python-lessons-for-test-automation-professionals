def register(func):
    print("running registation (%s)"%func.__name__)
    return func

@register
def func1():
    print("func1")

func1()
