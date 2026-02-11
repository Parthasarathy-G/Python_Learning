class Parent():

    def public_var(self):
        print("Public method")

    def _protected_var(self):
        print("Protected method")
    
    def __protected_var(self):
        print("Protected method")

    def access(self):
        self.public_var()
        self._protected_var()
        self.__private_var()
    