def decoratorp(a, b):
    def decoratori(func):
        print(a,b)
        return func
    return decoratori

@decoratorp(4,5)
def Func():
    pass
