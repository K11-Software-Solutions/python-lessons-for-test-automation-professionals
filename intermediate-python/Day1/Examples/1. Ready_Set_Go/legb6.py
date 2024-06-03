a_var = "global value"

def outer():
    a_var = "local value"
    print("outer before:", a_var)

    def inner():
        nonlocal a_var
        a_var = "local value 2"
        print("in inner():", a_var)
    inner()
    print("outer after:", a_var)

outer()
