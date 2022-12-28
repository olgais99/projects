class Swimmable:
    def __init__(self, name):
        self.name = name 

    def greeting(self):
        print(f'Hello, my name is {self.name} and i can swim')


class Walkable:
    def __init__(self, name):
        self.name = name 

    def greeting(self):
        print(f'Hello, my name is {self.name} and i can walk')


class Flyable:
    def __init__(self, name):
        self.name = name 

    def greeting(self):
        print(f'Hello, my name is {self.name} and i can fly')     


class GameCharachter(Swimmable, Walkable, Flyable):
    def __init__(self, name):
        self.name = name 
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)


    def greeting(self):
        print(f'Hello, my name is {self.name}')    


james = GameCharachter('james')
james.greeting()

print(isinstance(james, Walkable))   # является ли джеймс обьектом класса