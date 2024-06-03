import sys
def unhandled_exception(exception_type, exception_object, \
        exception_traceback):
     print("Uncaught exception")
     print("==================\n")
     print(exception_type.__name__)
     print(exception_object.args)
     print("\n++++++++++++++++++\n")
     print(exception_traceback.print_stack())
sys.excepthook = unhandled_exception

if __name__ == "__main__":
    raise RuntimeError("Test unhandled")
