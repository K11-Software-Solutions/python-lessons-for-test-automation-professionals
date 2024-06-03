class decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        self.func(*args)
        print(f"{args[0] + args[1]}")

@decorator
def func(x,y):   # resolve to decObj
    print(f"{x} + {y} = ",end="")

if __name__ == '__main__':
    func(1,2)
