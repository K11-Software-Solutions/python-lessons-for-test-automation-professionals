def FuncA():
    file=open(r"c:\code\data.txt")  
    try:
        pass # do something
    except Exception:  
        pass
    finally:
        file.close()

FuncA()