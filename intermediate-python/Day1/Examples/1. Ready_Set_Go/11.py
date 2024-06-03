'''
A module can run independently or imported as a library. 
Main should be the entry point only if the module is started independently not imported.  
This can be confirmed with the module variable __name__. 
If __name__ ==  “__main__”, the module is running independently and the entry method (i.e.,  main) should be called.
'''

import sys
def main():
    print("in main")
    
if  __name__ == "__main__":
    sys.exit(main())
