#Step 1: Defining an 'animal' class, working through the things with the instructor

class Animal(object):
    
    def __init__(self,age):
        self.age = age
        self.name = None #IMP: name is a data attribute even though an instance is not
                         #     initialized with it as the parameter   
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, newage):
        self.age = newage
        
    def set_name(self, newname = ""): # "" is the default binding
        self.name = newname
        
    def __str__(self):
        return "animal:" + str(self.name)+":"+ str(self.age)
    
#Step 2: Using/exploring the class
myAnimal = Animal(3)
print(myAnimal)


myAnimal.set_name('foobar')
myAnimal.get_age()


#Step 3: Creating an inherited classes "Cat", "Rabbit" and "Person"

class Cat(Animal):
                     # "init" is borrowed from the parent class 
    def speak(self): # new method for this class
        print("meow")
        
    def __str__(self):
        return "cat:" + str(self.name)+":"+ str(self.age) #overriding the print method
    
    

class Rabbit(Animal):
                     # "init" is borrowed from the parent class 
    def speak(self): # new method for this class
        print("meep")
        
    def __str__(self):
        return "rabbit:" + str(self.name)+":"+ str(self.age) #overriding the print method
        

class Person(Animal):
                      
    def __init__(self,name,age):
        Animal.__init__(self,age)  #call Animal's constructor
        Animal.set_name(self,name) #call Animal's method
        self.friends = []  #add a new data atttribute
        
    def get_friends(self):
        return self.friends
    
    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
            
    def speak(self):
        print ("hello")
        
    def __str__(self):
        return "rabbit:" + str(self.name)+":"+ str(self.age) #overriding the print method
    

#Step 4: Create a new class "Student" which is inherited from "Person"
 
class Student(Person):
    
    def __init__(self,name,age,major = None): #important
        Person.__init__(self,name,age) #tricky
        self.major = major
       
