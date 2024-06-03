try:
    var1=5  
    var2=0  
    var1/=var2
# orphaned code
except ZeroDivisionError as e:  
    print(e)
# execution continues here
