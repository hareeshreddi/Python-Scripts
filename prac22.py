s = "this_is_a_sentence"
a = s.split("_")          # Break s at every space found
print(a)
# output : ['this', 'is', 'a', 'sentence']
tup=("kk",9.0,2+7j,'kkk')
"""
#tup.append(8)#AttributeError--tuple object has no attribute named append
#tup.insert(2,4)#AttributeError--tuple object has no attribute named insert similarly remove 
#del tup[2] #TypeError: 'tuple' object doesn't support item deletion #though we can use del tup  Similarly extend 
"""
print('abc',-4.24e93,18+6.6j,'xyz')
x, y = 1, 2;
print("Value of x , y : ", x,y)
print(tup)
tup2=[[5,6],'34']
tup2.extend(tup+(56,))
print(tup2)
tup2.extend([3,5])
print(tup2)

list1=[[2,3],[4,5],"sdc",{
        "name1" : 9999999999,
        "name2" : 9999999999,}]
print(list1[3])
tup11=(2,3,4)
l2=[23,"fgb"]
list1.extend([2]+[3,4]+["xcfv"]+l2)
print(list1)
#list1.extend(78) #type-error:int object is not iterable
list1.append([2]+[3,4]+["cggg"])
print(list1)
list1.extend("ADD") #Noerror--String is iterable
print(list1)
list1.append((4,5))
print(list1)
list1.remove([2,3])
print(list1)


tupp=([2,3],[4,5],"dfd",(5,8))
#tupp=tupp+([2,3]) #TypeError: can only concatenate tuple (not "list") to tuple
tupp=tupp+([2,3],)#Noerror---may be without comma it is unable to recognize in previous case
print(tupp[3][1]) #Noerror 
#tupp.remove([4,5])  #AttributeError: 'tuple' object has no attribute 'remove'


n = int(input("Enter the number of points : "))
points1= []
points2=[]
print("Enter 3 decimals separated by space for each point")

for i in range(n):
    print("Coordinates of point",i+1,":",end=" ")
    (x,y,z)= map(float,input().split())
    p = (x,y,z)
    points1.extend(p)
    points2.append(p)
	
print(points1)
print(points2)
