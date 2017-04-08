
runs = [ 78 , 93 , 69 , 84 , 48 ]
# runs[-1] refers to last element of list
print(runs[-1])     # 48
print(runs[-5])     # 78
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
a=7
for i in range(1,6,1):
    print(i,end=" ")
	
print(i)

for i in range(6,8,-1):
    print(i,end=" ")
print(i)
#sdcfv
""" sddc """
for k in range(45,36,-1):
    print(k)
print(k)
u=a+k
print(u)

for i in range(99, 0, -1):
    if i == 1:
        print('1 bottle of beer on the wall, 1 bottle of beer!')
        print('So take it down, pass it around, no more bottles of beer on the wall!')
    elif i == 2:
        print('2 more bottles of beer on the wall, 2 more bottles of beer!')
        print('So take one down, pass it around, 1 more bottle of beer on the wall!')
    else:
        print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
        print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))

a = [ -34 , -20 , -3 , 2 , 9 , 94 , 482 , 3693 ]
b = "this is a sentence"
e= ["let","us","see","all"]
c = a[:6]
d = b[3:]
k=  e[1:3]
print(c)        # Output : [-34, -20, -3, 2, 9, 94]
print(d)        # Output : s is a sentence
print(k)        # Output : ['us','see']
a = [ 3 , 6 , 1 , 0 ]
if 1 in a :
    print("present")
else:
    print("not present")
	
for i in a:
    if i == 2:
	    print(a[i],"of",i,"is","in")
    elif i == 3:
	    print(a[i],"of",i,"is","in")