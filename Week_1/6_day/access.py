class Parent():
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"
    
    def acess_from_class(self):
        print("Inside the class")
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)

class son(Parent):
    def acess_from_class(self):
        print("Inside the class")
        print(self.public_var)
        print(self._protected_var)
        try:
         print(self.__private_var)
        except AttributeError:
            print("Private variable cannot be viewed")

        print(self._Parent__private_var) #Name magaling
        
p = son()
p.acess_from_class()