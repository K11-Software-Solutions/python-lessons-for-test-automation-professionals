class XClass:

    def __init__(self,firstname,lastname):
        self.__firstname, self.__lastname = firstname, lastname

    
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        if not isinstance(value,str):
            raise ValueError("firstname must be a string")
        
        if len(value) == 0:
            raise ValueError("firstname cannot be empty")

        self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        if not isinstance(value,str):
            raise ValueError("lastname must be a string")
        
        if len(value) == 0:
            raise ValueError("lastname cannot be empty")

        self.__lastname = value