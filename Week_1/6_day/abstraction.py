from abc import ABC, abstractclassmethod

class Featureplan(ABC):
    @abstractclassmethod
    def login():
        pass
    @abstractclassmethod
    def logout():
        pass

    def checkout():
        pass

class Webpage(Featureplan):
    
    def login(self):
        print("Logged in successfully")

    def logout(self):
        print("Logged out successfully")

a = Webpage()
a.login()