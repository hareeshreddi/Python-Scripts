#sex="unknown"
def gender(sex="Unknown"):
    if sex=="m":
	    print(sex)
    elif sex=="f":
	    print(sex)
    else:
	    print(sex)
gender() #does not give error if we have given default argument else gives errors even if u have defined it earlier
def mindblow(a="hi",b=" this is ",c="hari"):
     print(a+b+c)
mindblow("hello")
mindblow(b=" i am ",c="hari") #this is rare.....how come b and c refers to b and c respectively in the function
mindblow("hello"," there is")
#print(b) #error:b is not defined
#print(c) #error:c is not defined
"""default values are evaulated only once """
def f(a, L=[]):#do not forget that list is a mutable object which is the cause of lines 24 and 26
    L.append(a)
    return L
print( f(1,[4,5])) #prints [4,5,1]
#print (f(2,67)) #Attributeerror:'int' object has no attribute named append
#print (f(3,"jk")) #Attributeerror:'str' object has no attribute named append
print(f(1))  #prints [1]
print( f(11,[22,33]))
print(f(2)) #even though there is one more call in b/n 25 and 27 lines prints [1,2]//default argument is mutable object

def f(a, x=5):
    x=x+3
    return x
#print( f(1,[4,5])) #error:can concatenate list(not 'int') with list 
#print (f(3,"jk")) #Attributeerror:'str' object has no attribute named append
print(f(1))  #prints 8
print(f(2)) #prints 8 only unlike previous case where L(default argument) is mutable object 

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print( f(1,[4,5])) #prints [4,5,1]
#print (f(2,67)) #Attributeerror:'int' object has no attribute named append
#print (f(3,"jk")) #Attributeerror:'str' object has no attribute named append
print(f(1))  #prints [1]
print( f(11,[22,33]))
print(f(2)) #even though there is one more call in b/n 44 and 46 lines prints [2] only not [1,2]//default argument is int which is not mutable object 
print( ['doesn\'t'])
print( ['\doesn"hj\'t'])