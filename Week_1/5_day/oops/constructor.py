class Student:
    def __init__(self, fname, age):
        self.name = fname
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Parthasarathy", 23)
s1.display()