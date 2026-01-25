from inheritance import dad

class son(dad):
    def factory(self):
        print("white")
        
    def house(self):
        print("yellow")

s=son()
s.factory()
s.house()