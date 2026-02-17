class MyClass:
    a = 10 # attribute references or class variable
    
    def hello(self): # instance method
        return 'hello'
    
obj = MyClass() # object reference or instance reference

print(obj.a) # This will also print 10, as 'a' can be accessed using the instance reference
print(obj.hello())
print(MyClass.a) # This will print 10, as 'a' is a class variable and can be accessed using the class name
print(MyClass.hello(obj))


class Student:
    def __init__(self, name, age):
        self.name = name # instance variable
        self.age = age   # instance variable
        
    def __str__(self):
        return f"Student(name = {self.name}, age = {self.age})"  
    
    def __repr__(self):
        return f"Student(name = {self.name}, age = {self.age})"
        
obj = Student("parth", 20) # obj is an instance object of the Student class
print(obj)
print(repr(obj))

