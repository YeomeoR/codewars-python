#FizzBuzz
for num in range(1,101):
    if num % 15 == 0:
        print('FizzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')
    else:
        print(num)
    
#Fibonacci Sequence
a,b = 0,1
for i in range(0,10):
    print(a)
    a,b = b, a+b
    
#List comprehensions
my_list = [1,2,3,4,5,6,7,8,9,10]
#square each number in the list in just one line
squares = [num*num for num in my_list]
print(squares)

#Generators

#Fibonacci generator
def fib(num):
    a,b = 0,1
    for i in range(0, num):
        yield "{}: {}".format(i+1,a) #yield shows it's a generator
        a,b = b, a+b
    
for item in fib(10):
    print(item)
    
#OOP
class Person(object):
    def __init__(self, name):
        self.name = name
        
    def reveal_identity(self):
        print (f"My name is {(self.name)}")
        
class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name
        
    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print(f"..And I am {(self.hero_name)}")
        
rob = Person('Rob')
rob.reveal_identity()

yeomeo = SuperHero('Rob', 'Yeomeo')
yeomeo.reveal_identity()
