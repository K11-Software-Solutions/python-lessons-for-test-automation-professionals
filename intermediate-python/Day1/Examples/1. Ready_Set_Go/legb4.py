a_var = "global value"

def a_func():
    global a_var
    a_var = "global value 2"
    print(a_var, "[ a_var inside a_func() ]")

print(a_var, "[ a_var outside a_func() ]")
a_func()
print(a_var, "[ a_var outside a_func() ]")
