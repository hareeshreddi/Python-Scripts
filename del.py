
runs = [ 78 , 93 , 69 , 84 , 48 ]
# runs[-1] refers to last element of list
print(runs[-1])     # 48
print(runs[-5],end=" ")     # 78
#print(runs[-6])    # list index out of range 
#runs.insert(45)    # insert takes exactly 2 arguments
#runs.append(8,67)   # append takes exactly 1 argument
"""for m in range(45,56,-1):
    print(m)        # does not print anything and does not even initialize m so gives errror in the next line
print(m)            # gives errror that m is not defined

for g in range(40,38,1):
    print(g)        # does not print anything and does not even initialize g so gives errror in the next line
print(g)            # gives errror that g is not defined

for l in range(45,45,+1/-1):
    print(l)        # does not print anything and does not even initialize l so gives errror in the next line
print(l)            # gives errror that l is not defined
"""
for l in range(45,48,+1):
    print(l)       
print(l)           
l=l+3 #No Error
print(l)

runs.append(56)
print(runs)
#runs.del(2) #invalid syntax
del(runs[2])
print(runs)
runs.pop(2) #removes runs[2]
print(runs)

a = [4, 5, 3]
#a.remove(7)
"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list"""
#del a[7]
"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range"""
#a.pop(3)
"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range"""
a.append(45)
a.insert(7,41) #no error though there are no elements b/n indices 4 and 6 41 is just added at index 4 as there are already 4 elements in the list
#print(a[5]) #list index out of bounds exception
print(len(a))
"""
#del a 
#print(a) #NameError: name 'a' is not defined"""

# Function to convert date from mm-dd-yyyy to dd-mm-yyyy format
def convert(old_date):
    print(old_date)
    l = list(old_date)          # Get the string in list form 
    print(l)
    l[0],l[3] = l[3],l[0]       # Swap first digits of date and month
    print(l)
    l[1],l[4] = l[4],l[1]       # Swap second digits of date and month
    print(l)
    new_date = ''.join(l)       # Convert list back into string
    return new_date

# Make a list of dates in mm-dd-yyyy format
date_list = ['08-13-2017' , "12-31-2016" , "01-26-2017" , "05-01-2016" ]
# Map the convert function on this list
converted_dates = list(map(convert,date_list))

print(converted_dates)


s = "49-+--+-3438-+-22-+-91"
aa = s.split("-+-")
print(aa)

d=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
s=d[:-99:-2]
print(s)

num1=int(input())
num=0
l=[]
def prin(a):
    k=0
    la=list(a)
    if len(la)!=0:
	    print(la[0],end="")
    for i in la:
        k=k+1
        if i==' ':
            if(la[k]!=' '):
                print(la[k],end="")
    print()
    return
while num<num1:
    l.append(input())
    num=num+1	
final=list(map(prin,l))