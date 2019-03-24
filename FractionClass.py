

#Version 3: a more formalised/elegant version of the above
"""
Incorporates getters and overriding of + operator
"""


#STEP1: Function for recursion - required to reduce gractions
def gcdRecur(a,b):
        
        if b%a==0:
            return a
        if a>=b:
            return gcdRecur(b,a%b)
        if b>a:
            return gcdRecur(b,a)

#STEP2: Defining the class 'fraction3'
            
class fraction3(object):
    
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom
        
    def __str__(self): #to print out the fraction in the convenional way
        return str(self.num) + " / " + str(self.denom)
    
    def get_num(self): #get method to uniquely access the numerator
        return self.num
    
    def get_denom(self):
        return self.denom
    
    def __add__(self,other): #the double underscore format enables overloading
        res_num = self.get_num()* other.get_denom() + other.get_num()* self.get_denom()
        res_denom = self.get_denom() * other.get_denom()
        
        factor = gcdRecur (res_num,res_denom)
        
        if res_num == res_denom:
            return int(res_num/factor)
        else:
            return fraction3(int(res_num/factor),int(res_denom/factor))
        
#STEP3: Implementation and testing    

#defining data objects
f5 = fraction3(1,2)
f6 = fraction3(1,4)
f7 = fraction3(3,4)


#overloading the + operator
print (f5 + f6 )
print (f6 + f7 )
print (f5 + f7 )
