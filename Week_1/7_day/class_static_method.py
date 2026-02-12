# class MyClass:
    
#     def instance_method(self):
#         print("Called instance method")
    
#     @classmethod
#     def class_method(cls):
#         print("Called class method")

#     @staticmethod
#     def static_method():
#         print("Called static method")

# obj = MyClass()
# obj.instance_method()
# MyClass.class_method()
# MyClass.static_method()

# Class method
# class Employee:
#     company_name = "OpenAi"

#     @classmethod
#     def change_company(cls, new_name):
#         cls.company_name = new_name

# Employee.change_company("Google")
# print(Employee.company_name)


#static method

class Math:
    @staticmethod
    def add(x, y):
        return x + y
print(Math.add(10,5))