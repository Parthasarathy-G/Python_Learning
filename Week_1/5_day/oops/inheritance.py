class dad: # parent
    def house(self):
        print ("I am from dad class")
    
class son(dad): #child

    def factory(self):
        print("I am factory class")
    
s = son()
s.house()