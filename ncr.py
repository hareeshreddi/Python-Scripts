def factorial(n):
    p = 1
    for i in range(2,n+1):
        p *= i

def nPr(n,r):
    answer = factorial(n) / factorial(r)
    return answer
	
def nCr(n,r):
    answer = factorial(n) / ( factorial(r) * factorial(n-r) )
    return answer

print("Enter n : ",end="")
n = int(input())
print("Enter r : ",end="")
r = int(input())

if n<r or r<0 :
    print("Invalid n/r")
else:
    result1 = nCr(n,r)
    result2 = nPr(n,r)
    print(n,"C",r,"=",result1)
    print(n,"P",r,"=",result2)