class Animal:
    def __init__(self,name):
        self.name = name
    
    def __str__(name):
        return name
    
    def introduce(self):
        print(f"I'm {self.name}!!")    
        
    def speak(self):
        print('The animal is cominicating....')
        


class Cao(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name)
        self.breed = breed
        self.age = age

    def __str__(name,breed):
        return super().__str__(breed)
    
    def __int__(age):
        return age
    
    def introduce(self):
        print(f"I'm a Dog named {self.name}, my breed is {self.breed}, and I'm {self.age} years old!" )
        
    def speak(self):
        print('Woof Woof')
    
    
class Gato(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name)
        self.breed = breed
        self.age = age
        
    def __str__(name,breed):
        return super().__str__(breed)
    
    def __int__(age):
        return age

    def introduce(self):
        print(f"I'm a Cat named {self.name}, my breed is {self.breed}, and I'm {self.age} years old!" )
        
    def speak(self):
        print('Miau Miau')
        
tartaruga = Animal('Alfredo')
Cao = Cao('Yara', 'Yorkshire', 8)
Gato = Gato('Cucumber', 'Maine Coon', 6)


print('------------')
tartaruga.introduce()
tartaruga.speak()
print('------------')
Cao.introduce()
Cao.speak()
print('------------')
Gato.introduce()
Gato.speak()
print('------------')