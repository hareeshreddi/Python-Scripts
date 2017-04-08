def create_3_tuple(*arg):
  list1=[]
  list2=[]
  temp=1
  while temp!=6:
    list2.append(arg[0][temp])
    temp=temp+1 
  list2=tuple(list2)
  list1.append(list2)
  temp=2
  list2=list(list2)
  list2=list2[3:6:1]
  while temp!=7:
    list2.append(arg[0][temp])
    temp=temp+1
  list2=tuple(list2)
  list1.append(list2)
  return list1
listl=create_3_tuple((1,2,3,4,3,6,7))
print(listl)


def create_3_1_tuple(arg1):
  list1=[]
  list2=[]
  temp=1
  while temp!=6:
    list2.append(arg1[temp])
    temp=temp+1 
  list2=tuple(list2)
  list1.append(list2)
  temp=2
  list2=list(list2)
  list2=list2[3:6:1]
  while temp!=7:
    list2.append(arg1[temp])
    temp=temp+1
  list2=tuple(list2)
  list1.append(list2)
  return list1
list11=create_3_1_tuple((1,2,3,4,3,6,7))
print(list11)

x=3
x=x+(3)
print(x)
z=type((3)) is int 
print(z)
j=(4,8)
j=j+tuple("7")
print(j)


def create_3_1_tuple(arg):
  list1=[]
  list2=[]
  temp=1 
  while temp!=7:
    list2.append(arg[temp])
    if len(list2)==3:
      temp-=2
      list2=tuple(list2)
      list1.append(list2)
      list2=list(list2)
      list2=list2[3:4]
    temp+=1 
  return list1

list22=create_3_1_tuple([1,2,3,4,3,6,7])
print(list22)