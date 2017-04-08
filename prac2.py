num1=int(input())
num2=int(input())
num3=input()
if num3=="+":
   print("Sum is"+str(num1+num2))
elif num3=="-":
   print("diff is"+str(num1-num2))
elif num3=="/":
   print("div is"+str(num1/num2))
else:
	print("rem is"+str(num1%num2))
print("enter n value::")
n=int(input())
for i in range(1,11,2):
	print(str(n)+"*"+str(i)+"="+str(n*i))
	print(n,"*",i,"=",n*i,end="   ")

for i in range(1,n+1):
    for j in range(1,i+1):
	      print("*",end="")
    print("\n")
	  
num=1
den=1
ans=0

for i in range(1,n+1):
    term=num/den
    ans=ans+term
    num=num*i
    den=den*i
print(ans)
