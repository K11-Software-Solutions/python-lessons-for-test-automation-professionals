def deco(func):
        def inner():  # does the work
            func()
            print("running registation (%s)"%func.__name__)
        return inner

@deco
def target():
    print("running target")

target()
