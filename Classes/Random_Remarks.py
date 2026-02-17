# Function defined outside the class
def f1(self, x, y):
    return max(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'
    h = g
    
obj = C()
print(obj.f(10, 20))
print(obj.h())  

class MyClass:

    def __init__(self):
        self.data = []
        
    def add(self, x):
        self.data.append(x)
        
    def display(self, x):
        self.add(x)    
        self.add(x)    

obj = MyClass()
obj.display(10)
print(obj.data)  # This will print [10, 10] as the display method