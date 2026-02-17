class perent:
    
  def speak(self):
    print("I am a perent")
    
class child(perent):
    pass

obj = child()
obj.speak()

# Method overriding
class Person:
    def speak(self):
        print("Hello")

class Student(Person):
    def speak(self):
        super().speak()
        print("Hi, I am a student")

s = Student()
s.speak()

    