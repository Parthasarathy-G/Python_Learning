# class grandfather(self):

#     def car(self):
#         print("red car")

# Multiple inheritance
# class dad(): # parent
#     def house(self):
#         print ("house white")

# class son1 (dad):

#     def factory(self):
#         print("Factory")
# class son2 (dad):

#     def market(self):
#         print("market")
    
# g = son1()
# g.house()
# g.factory()

# v = son2()
# v.house()
# v.market()

#Multiple level inheritance
class dad(): # parent
    def house(self):
        print ("house white")
class mom(): # parent
    def car(self):
        print ("red car")

class son1 (dad, mom): # can give two parent class  

    def factory(self):
        print("Factory")
    
g = son1()
g.house()
g.factory()
g.car()




# class dad: # parent
#     def house(self):
#         print ("I am from dad class")
    
# class son(dad): #child

#     def factory(self):
#         print("I am factory class")
    
# s = son()
# s.house()