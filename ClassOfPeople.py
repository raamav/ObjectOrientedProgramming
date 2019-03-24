

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
