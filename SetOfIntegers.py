
"""
Creating a basic intSet class that supports the following methods
    insert() - inserting an element ONLY if its not there
    isMember() - checking if an integer is a part of intSet
    remove() - removing an element if its present else raising ValueError exception
    getMembers() - getting a list of members of intSet 
"""

#Implementing Class
class intSet(object):
    
    def __init__(self):
        """creating an empty set of integers"""    
        self.vals = []
        
    def insert(self,e):
        if e not in self.vals:
            self.vals.append(e)
            
    def isMember(self,e):
        if e in self.vals:
            return True
        else:
            return False
        
    def remove(self,e):
        try:
            self.vals.remove(e)
        except ValueError:
            print("Not in list ")
            
    def getMembers(self):
        print(self.vals)


#Experimenting with Class

x= intSet() #x is an object of type intSet
type(x) #validating the above

x.insert(1) #inserting a set of values in x
x.insert(1)
x.insert(3)
x.insert(5)
x.insert(5)

x.getMembers() #getting a list of members of x

x.remove(9) #removing a member thats not there in the list
x.remove(1) #removing a member thats present in the list

x.getMembers() #checking if the functions work as per specification
