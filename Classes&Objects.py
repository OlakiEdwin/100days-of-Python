class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
            print(self.name  + ' is walking...')

    def speak(self):
            print('Hello my name is ' + self.name + ' and I am ' + str(self.age) + ' years old')

john = Person('John', 22)
mariam = Person('Mariam', 20)

print(john.name + ' ' + str(john.age))
john.speak()
john.walk()

print(mariam.name + ' ' + str(mariam.age))
mariam.speak()
mariam.walk()