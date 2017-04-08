def create_33_tup(arg):
  temp=1
  while temp<=4:
    yield arg[temp:temp+3]
    temp+=1
  temp=1
  while temp<=2:
    yield arg[temp:temp+3]
    temp+=1

def create_33_tup(arg):
	list1=[]
	temp=1
	while temp<=4:
		list1.append(arg[temp:temp+3])
		temp+=1
	temp=1
	while temp<=2:
		list1.append(arg[temp:temp+3])
		temp+=1
	return list1