class dad:
    def factory(self):
        print("Have access to factory")
    
    def house(self):
        print("I own a house")
    

class son(dad):

    def car(self):
     print("Have access to car")

a = son()
a.house()