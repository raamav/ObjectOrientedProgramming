

"""
Creating a 'Person' class which incorporates the following features:
    Data: accept name (firstName, lastName) and birthday (optional)
    Methods:
        'Getter' methods for name and lastName; getName() and getLastName()
        'Setter' method for birthdate, setBirthdate()
        Retrieving age of the individual, getAge()
        Ability to sort the records by the lastName; override "<" and sort()
"""

import datetime

class Person(object):
    
    def __init__(self,name):
        self.name = name
        self.birthday = None
        try:
            self.lastName = self.name.split(sep = " ")[-1]
        except:
            self.lastName = None
            
    def getName(self):
        return self.name
    
    def getLastName(self):
        return self.lastName
    
    def setBirthdate(self,birthday):
        self.birthday = birthday
        
    def getAge(self):
        if self.birthday == None:
            print("immortal ")
        else:
            days = (datetime.date.today()- self.birthday).days
            years = int(days/365)
            return years
        
    def __lt__(self,other):
        if self.lastName == other.lastName:
            return self.name < other.name
        else:
            return self.lastName < other.lastName
        
    def __str__(self):
        return self.name
        
        
            
#creating instances
one = Person("Rama Vishwanathan")
two = Person("Jaishree Vishwanathan")
three = Person("Appa Vishwanathan")
four = Person("Anil Barot")
five = Person("Bhadra Lang Ankur")

print(one)
print(two)

one.setBirthdate(datetime.date(1983,7,18))        
two.setBirthdate(datetime.date(1988,11,12))
    
    

#testing methods

one.getAge()
two.getAge()
three.getAge()   

#checking if the sort functionality works
pList = [one,two,three,four,five]  

for p in pList: #initial state
    print (p)
    
pList.sort() #the sorting function

for p in pList: #final state
    print (p)

    
"""
Creating a sub-class MITPerson that has the following properties:
    - assigning ID numbers in sequence
    - get ID number
    - sort by ID number (as opposed to doing it by the last namein the parent class)
"""

class MITPerson(Person):
    
    nextIdNum = 0        #This is a class variable
    
    def __init__(self,name):
        Person.__init__(self,name)  #Calling the parent class to set-up the initialization stuff
        self.IdNum = MITPerson.nextIdNum #creating an ID variable for the instance
        MITPerson.nextIdNum +=1  #incrementing the ID for subsequent instance

    def getIdNum(self):
        return self.IdNum    
    
    #sorting the MITPerson by their ID and not by their name; ovveriding __lt__
    def __lt__(self,other):
        return self.IdNum < other.IdNum
    
    #creating an additional "speak" method
    def speak(self,uttarance):
        return (self.getLastName() + " says: " + uttarance)


#create a few objects
six = MITPerson("Eric Grimson")
seven = MITPerson("Steve Guttag")
eight = MITPerson("Anna Bell")

print(six)

#checking if sort functionality works
pList = [six, seven,eight]  

for p in pList: #initial state
    print (p)
    
pList.sort() #the sorting function

for p in pList: #final state
    print (p)

#more checks
eight.getIdNum()

six.speak("This is very cool")





"""
Creating a sub-class Professor (parent class MITPerson) with the following properties:
    - Every professor has a department
    - speaks differently, ovverride the speak() method
    - also has a lecture defined; lecture()
"""

class Professor(MITPerson):
    
    def __init__(self,name,department):
        MITPerson.__init__(self,name) #inherit from the super class
        self.department = department #add another attribute
        
    def speak(self,uttarance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self,new + uttarance)
    
    def lecture (self,topic):
        return self.speak('it is obvious that ' + topic)


#testing
nine = Professor("GKS Suresh","Electronics and Telecoomunication")
print(nine)

nine.speak("Hello Students ")
nine.lecture("Microprocessors")

# This is a super comprehensive example that demonstrates how inheritance works

