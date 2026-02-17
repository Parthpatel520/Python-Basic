class MyClass:
    a = 10
    car_names = []
    
    def __init__(self, name):
        self.name = name
        
    def car(self, car_name):
        self.car_names.append(car_name)

obj = MyClass("parth")
print(obj.a)
print(obj.name)

x = MyClass("kunj")
print(x.name)

obj.car("BMW")
print(obj.car_names)
x.car("Audi")

print(obj.car_names) 
