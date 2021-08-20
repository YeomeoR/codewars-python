class Pet:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
class Cat(Pet):
    def speak(self):
        print('Meow')
        
class Dog(Pet):
    def speak(self):
        print('Woof')

d = Dog("Magnus", 1)
print(d.speak())

class Robot:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    def introduce_self(self):
        print(f"My name is {self.name}, I am {self.color} and I am {self.weight}llbs")
        
r1 = Robot("Rob","red",30)
r2 = Robot("Jerry","blue",35)

r1.introduce_self()
r2.introduce_self()