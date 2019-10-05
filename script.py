cadena = "esto es una cadena"

""" print(cadena)

for c in cadena:
    print(c)
 """
class Dog:
    """ 
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def say_hello(self):
         return f'hi i am {self.name}'


#instance
puppet = Dog("teodoro",10)

#getter
print(puppet.name)