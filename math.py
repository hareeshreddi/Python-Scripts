# Import math module containing many mathematical functions
import math

a = 16
b = math.sqrt(a)   # Use the square root function from math module
print(b)

print(math.pi)
print(math.e)
# Import sin, cos functions from math module
from math import sin,ceil
# Now, instead of math.sin(), we can directly use sin()
a = 1.123
b = sin(a)
c = ceil(a)
print(b)
print(c)
#Using split function 
a = input().split(" ")
print(a)
b = list( map(int,a) )
# Sample input:  4 3 -2 9 0 10
# a will become : ['4', '3', '-2', '9', '0', '10']
# b will become : [4, 3, -2, 9, 0, 10]
print(a)
print(b)
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [8, 9, 10]
for i in list2: #Iterating through individual elements in list2
           list1.append(i) #Appending these individual elements to list1

print(list1)
list11=[33];
list1.append(list11)
print(list1)
x=range(1,45)
print(x)
list1.insert(2,[34,78])
print(list1) 
def cube(n):
    return n*n*n

a = [ 3 , 1 , 6 , 8 , 2 ]
b = map( cube , a )
b = list(b)
print(b)
def cube(n):
    return n*n*n

a = [ 3 , 1 , 6 , 8 , 2 ]
b = str(a)
print(b)
runs = [ 78 , 84 , 69 , 84 , 48 ]
runs.remove(84)    # Remove the first 84 in the list
print(runs)
runs.extend([5,84,"jk","a[1]"])
#runs.remove(a[1])  #only used to remove a value by mentioning its amount like 84
#runs.del(69)       #only used to delete a value by mentioning its index like a[1]
del a[2]
print(runs)

print("Enter the number to convert")
n = int(input())

answer = []

while n>0:
    digit = n%2
    answer = answer + [digit]
    n = int(n/2) #if u remove the int then u will see the magic:p
print(answer)