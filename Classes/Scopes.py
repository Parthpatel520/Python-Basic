global x
x = 10 # Global variable
y = 20 # Global variable

class MyClass:
    z = 40 #Enclosing variable (class NameSpace using self.z)

    def method(self):
        x = 30 #local variable
        print("Local variable x:", x)  # This will print 30  
        print("global variable:", y)  # This will print 20
        print("Enclosing variable z:", self.z)  # This will print 40
        
obj = MyClass()
obj.method()  # This will call the method and print 30

print("--- Testing nested scope ---")

a = 10 # Global variable

class scope:
    
    print("Global variable a:", a)  # This will print 10
    
    def local_scope(self):
        a = 50 #local variable
        print("Local variable a:", a)  # This will print 50
        
        def nested_scope(self):
            b = 60 #nested local variable
            print("Nested local variable b:", b)  # This will print 60
            print("Accessing local variable a from nested scope:", a)  # This will print 50
        nested_scope(self)
        
        def nonlocal_scope(self):
            nonlocal a
            a = 70 # This will modify the local variable a in the enclosing scope
            print("Modified local variable a using nonlocal:", a)  # This will print 70
        nonlocal_scope(self)  
        
        print("modified local variable a *******:", a)  # This will print 70 (modified by nonlocal_scope)
        
        def global_scope(self):
            global a
            a = 80 # This will modify the global variable a
            print("Modified global variable a using global:", a)  # This will print 80
        global_scope(self)     
    print("** Global variable a after modification: **", a)  # This will print 80 (modified by global_scope)
            
obj2 = scope()
obj2.local_scope()  # This will call the local_scope method and print 50 and 60
print("*** Global variable a after modification: ***", a)  # This will print 80 (modified by global_scope)


print("------- Instance variable --------")

class Test:
    def __init__(self):
        self.x = 10

    def change(self):
        self.x = 20
    
    def display(self):  
        print("Value of self.x in display method:", self.x)  # This will print 20 (instance variable)

t = Test()
t.change()
t.display()
print("Initial value of x:", t.x)  # This will print 20 (instance variable)
